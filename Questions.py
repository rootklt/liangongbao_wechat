import json


class Questions:
    def __init__(self, filename='answer.json', unkown_ques='unkown_ques.json') -> None:
        self.filename = filename
        self.unkown_ques = unkown_ques
        self.answersDict = {}
        self.initAnswers()

    def initAnswers(self):
        with open(self.filename, encoding='utf-8', mode='r') as f:
            self.answersDict = json.load(f)

    def getAnswer(self, question):
        return self.answersDict[question] if question in self.answersDict else None

    def write_unkown_ques(self, data=None):
        if not data:
            return
        with open(self.unkown_ques, encoding='utf-8', mode='r+') as f:
            content = f.read()
            if data.get('content') in content:
                return
            f.write(json.dumps(data, ensure_ascii=False)+',\n')
