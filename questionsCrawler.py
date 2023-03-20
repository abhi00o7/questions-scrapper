import json
from requests_html import HTMLSession

session = HTMLSession()

# nda questions website url
req = session.get('https://www.4ono.com/nda-english-test/')

spottingErrSelector = 'body > div.box.article_page > div.o_center > article > div > ol:nth-child(5) > li:nth-child(2)'
antonymsSelector = 'body > div.box.article_page > div.o_center > article > div > ol:nth-child(6)'
synonymsSelector = 'body > div.box.article_page > div.o_center > article > div > ol:nth-child(7)'
fillBlanksSelector = 'body > div.box.article_page > div.o_center > article > div > ol:nth-child(8)'
sentenceImprovementSelector = 'body > div.box.article_page > div.o_center > article > div > ol:nth-child(9)'
sequenceSelector = 'body > div.box.article_page > div.o_center > article > div > ol:nth-child(10)'

reqQuestionsOptions = req.html.find(sequenceSelector, first=True)

questionsList = reqQuestionsOptions.find('li > p')
options = reqQuestionsOptions.find('li > ol')


def correctOpt(str):
    if str in optionsList[4].text:
        return True
    return False


QuestionsList = []
# def getQuestionsAnswers(selector):
for index, question in enumerate(questionsList):
    optionsList = options[index].find('li')
    optionsData = [
        {
            "id": 1,
            "label": "A",
            "text": optionsList[0].text,
            "isCorrect": correctOpt(optionsList[0].text)
        },
        {
            "id": 2,
            "label": "B",
            "text": optionsList[1].text,
            "isCorrect": correctOpt(optionsList[1].text)
        },
        {
            "id": 3,
            "label": "C",
            "text": optionsList[2].text,
            "isCorrect": correctOpt(optionsList[2].text)
        },
        {
            "id": 4,
            "label": "D",
            "text": optionsList[3].text,
            "isCorrect": correctOpt(optionsList[3].text)
        }
    ]
    questionsData = {
        "id": index+1,
        "text": question.text,
        "options": optionsData
    }

    QuestionsList.append(questionsData)

# print( len(QuestionsList))

# questionsJsonData = json.dumps(QuestionsList)
# print(questionsJsonData)

# write data to json format

with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(QuestionsList, f, ensure_ascii=False, indent=2)

'''
1. Get questions one by one
2. Set OptionsList to same index as question
3. Set options from one to four
4. Use Options Object to set optionsData
5. Use Question dict to set Question and optionsData
6. Push the Question to the topic Array
'''

# Options Data BluePrint || set the data to json string
# optionsData = [
#     {
#         "id": 1,
#         "label": "A",
#         "text": "",
#         "isCorrect": False
#     },
#     {
#         "id": 2,
#         "label": "B",
#         "text": "",
#         "isCorrect": False
#     },
#     {
#         "id": 3,
#         "label": "C",
#         "text": "",
#         "isCorrect": False
#     },
#     {
#         "id": 4,
#         "label": "D",
#         "text": "",
#         "isCorrect": False
#     }
# ]

# Question Data BluePrint
# questionsData = {"id": 1,
#                  "text": "",
#                  "options": optionsData}
