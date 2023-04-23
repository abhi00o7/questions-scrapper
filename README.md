# Questions and Answers web crawler

---

This is a web crawler made with python using requests_html module.

## steps to start

    * Get websites URL
    * Set website URL 

## Run on terminal

```python
 > py questionsCrawler.py
```

## Data Gathering Structure 

```json
{
   "questionsData":{
      "id":1,
      "text":"",
      "options":[
         {
            "id":1,
            "label":"A",
            "text":"",
            "isCorrect":false
         },
         {
            "id":2,
            "label":"B",
            "text":"",
            "isCorrect":false
         },
         {
            "id":3,
            "label":"C",
            "text":"",
            "isCorrect":false
         },
         {
            "id":4,
            "label":"D",
            "text":"",
            "isCorrect":false
         }
      ]
   }
}
```

## Data Gathering Structure 

```json
{
   "questionsData":{
      "id":1,
      "text":"",
      "options":[
         {
            "id":1,
            "label":"A",
            "text":"",
            "isCorrect":false
         },
         {
            "id":2,
            "label":"B",
            "text":"",
            "isCorrect":false
         },
         {
            "id":3,
            "label":"C",
            "text":"",
            "isCorrect":false
         },
         {
            "id":4,
            "label":"D",
            "text":"",
            "isCorrect":false
         }
      ]
   }
}
```

## code Description

    * This code is used to scrape the questions and answers from 4ono.com
    * The website is a website dedicated to NDA exam preparation
    * The website contains all the questions and answers for the NDA exam
    * The code is written in Python 3.7
    * The code is using requests_html library to scrape the questions and answers from the website
    * The code is using json library to store the questions and answers in a json format
    * The code is using for loop to iterate over the list of questions and answers
    * The code is using if else statements to check if the answer is correct or not
    * The code is using append function to append the questions and answers to the list
    * The code is using with open function to write the list to a json file
