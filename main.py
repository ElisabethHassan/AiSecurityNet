import requests
from flask import Flask, request, render_template


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        value = request.form.get('textbox')
        url = "https://ai-content-detector-ai-gpt.p.rapidapi.com/api/detectText/"
        payload = { "text": value}
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
        return render_template('layout.html', value=value, ai_prob=ai_prob, human_prob=human_prob, ai_words=ai_words, total_words=total_words)

    return render_template('layout.html')


if __name__ == '__main__':
    app.config['SECRET KEY'] = 'DFJASLJKDLASJLKF'
    app.run(debug=True, host='0.0.0.0', port='8080')