import requests
from flask import Flask, request, render_template

# url = "https://ai-content-detector2.p.rapidapi.com/analyzePatternsAndPerplexities"
#
# payload = { "text": "Mahendra Singh Dhoni, popularly known as MS Dhoni, is a legendary cricketer and former captain of the Indian national cricket team. He is widely regarded as one of the greatest cricketing minds of all time and is considered a true icon of the sport. Dhoni's journey in cricket has been nothing short of extraordinary, and his achievements both on and off the field have made him a true inspiration to millions of people around the world. Dhoni was born on July 7, 1981, in Ranchi, a small city in the eastern part of India. He grew up in a modest household and was a multi-talented athlete from a young age. Dhoni was particularly interested in cricket, and he spent hours playing with his friends on the streets and in local cricket academies. His hard work and dedication eventually paid off when he was selected to play for the Bihar Under-19 team." }
# headers = {
#     "content-type": "application/json",
#     "X-RapidAPI-Key": "964ed1fefamsh5eeec8570982bc1p196f73jsn0febe306318f",
#     "X-RapidAPI-Host": "ai-content-detector2.p.rapidapi.com"
# }

# response = requests.post(url, json=payload, headers=headers)
# data = response.json()
#
# print(data['data']["AI"])

app = Flask(__name__)
@app.route('/')
def home():
    return render_template('layout.html')


if __name__ == '__main__':
    app.config['SECRET KEY'] = 'DFJASLJKDLASJLKF'
    app.run(debug=True, host='0.0.0.0', port='8080')