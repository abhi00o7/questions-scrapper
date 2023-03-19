import json
import requests
from bs4 import BeautifulSoup

with open('quizData.json') as f:
    quizData = json.load(f)


url = 'https://www.4ono.com/nda-english-test/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

questions = soup.find_all('div', class_='entry-content')
for question in questions:
    question_text = question.find('h3').text
    options = question.find_all('li')
    for option in options:
        option_text = option.text
        print(option_text)


# set the data to json string
optionsData = [
    {
        "id": 1,
        "label": "A",
        "text": "",
        "isCorrect": False
    },
    {
        "id": 2,
        "label": "B",
        "text": "",
        "isCorrect": False
    },
    {
        "id": 3,
        "label": "C",
        "text": "",
        "isCorrect": False
    },
    {
        "id": 4,
        "label": "D",
        "text": "",
        "isCorrect": False
    }
]

questionsData = [
    {id: 1,
     "text": "",
     "options": optionsData}
]

# print(type(quizData))
# print(json.dumps(optionsData, indent=2))
# print(optionsData[3]['id'])
# print(json.dumps(quizData, indent=2))


# print(json.dumps(quizData[0].questions, indent=2))
