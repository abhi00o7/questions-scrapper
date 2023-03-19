from bs4 import BeautifulSoup
import json

with open('quizData.json') as f:
    quizData = json.load(f)



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
print(json.dumps(optionsData, indent=2))
print(optionsData[3]['id'])
# print(json.dumps(quizData, indent=2))


# print(json.dumps(quizData[0].questions, indent=2))
