import json


class Questions:
    def __init__(self, filename='answer.json') -> None:
        self.filename = filename
        self.answersDict = {}
        self.initAnswers()

    def initAnswers(self):
        with open(self.filename, encoding='utf-8', mode='r') as f:
            self.answersDict = json.load(f)

    def getAnswer(self, question):
        return self.answersDict[question] if question in self.answersDict else None
