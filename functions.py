import json
from random import shuffle


class Functions():

    def handleJson(jsonPath):
        jsonData = open(jsonPath, 'r', -1, 'UTF-8').read()
        myJson = json.loads(jsonData)
        result = Functions.assignValues(myJson)
        return result

    def assignValues(QJson):
        newJson = QJson
        value = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
        shuffle(value)  # Reordenar aleatoriamente.

        for cat in newJson:
            now = 0
            for quest in newJson[cat]['preguntas']:
                if now < len(value):
                    quest['value'] = value[now]
                    now += 1
        return newJson