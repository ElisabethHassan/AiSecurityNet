import os
import requests
from flask import Flask, request, render_template, g
import sqlite3
from helper import pdf

app = Flask(__name__, template_folder='templates')
app.config['DATABASE'] = 'database.db'
app.config['SECRET_KEY'] = 'DFJASLJKDLASJLKF'

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(app.config['DATABASE'])
    return g.db

def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()

def create_table():
    db = get_db()
    c = db.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS past_files (name TEXT, ai_probability REAL)")
    db.commit()

# page for pdf files
@app.route('/pdf', methods=['GET', 'POST'])
def pdf_page():
    if request.method == 'POST':
        file = request.files['document']
        
        if file.filename == '':
            return render_template('layout.html', error_message='No file selected.')
        
        file_path = 'uploaded_files/' + file.filename

        # Create the 'uploaded_files' directory if it doesn't exist
        os.makedirs('uploaded_files', exist_ok=True)

        file.save(file_path)
        val = pdf(file_path)  # Pass the file path to the pdf() function
        
        if not val:
            return render_template('layout.html', error_message='PDF file could not be processed.')

        url = "https://ai-content-detector-ai-gpt.p.rapidapi.com/api/detectText/"
        payload = {"text": val}
        headers = {
            "content-type": "application/json",
            "Content-Type": "application/json",
            "X-RapidAPI-Key": "b6c8bcae61msh708d041562ba044p18d7cdjsn3385f1eca732",
            "X-RapidAPI-Host": "ai-content-detector-ai-gpt.p.rapidapi.com"
        }

        response = requests.post(url, json=payload, headers=headers)
        data = response.json()
        print(data["fakePercentage"])
        ai_prob = data["fakePercentage"]
        human_prob = 100 - ai_prob
        total_words = data['textWords']
        ai_words = data['aiWords']

        # Save the analysis results to the database
        db = get_db()
        c = db.cursor()
        c.execute("INSERT INTO past_files (name, ai_probability) VALUES (?, ?)", (file.filename, ai_prob))
        db.commit()

        return render_template('demo.html', value=val, ai_prob=ai_prob, human_prob=human_prob, ai_words=ai_words, total_words=total_words)
    
    return render_template('layout.html')

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        val = request.form.get('textbox')
        name = request.form.get('name')  # Get the value from the "name" input field
        
        if not val:
            return render_template('layout.html', error_message='No text entered.')
        
        url = "https://ai-content-detector-ai-gpt.p.rapidapi.com/api/detectText/"
        payload = {"text": val}
        headers = {
            "content-type": "application/json",
            "Content-Type": "application/json",
            "X-RapidAPI-Key": "b6c8bcae61msh708d041562ba044p18d7cdjsn3385f1eca732",
            "X-RapidAPI-Host": "ai-content-detector-ai-gpt.p.rapidapi.com"
        }
        response = requests.post(url, json=payload, headers=headers)
        data = response.json()
        ai_prob = data["fakePercentage"]
        human_prob = 100 - ai_prob
        total_words = data['textWords']
        ai_words = data['aiWords']
        db = get_db()
        c = db.cursor()
        c.execute("INSERT INTO past_files (name, ai_probability) VALUES (?, ?)", (name, ai_prob))  # Use the 'name' variable
        db.commit()
        return render_template('demo.html', value=val, ai_prob=ai_prob, human_prob=human_prob, ai_words=ai_words, total_words=total_words)
    return render_template('layout.html')


@app.route('/past-files')
def past_files():
    db = get_db()
    c = db.cursor()
    c.execute("SELECT * FROM past_files")
    files = c.fetchall()
    return render_template('past_files.html', files=files)

if __name__ == '__main__':
    with app.app_context():
        create_table()
    app.teardown_appcontext(close_db)
    app.run(debug=True, host='0.0.0.0', port='5000')
