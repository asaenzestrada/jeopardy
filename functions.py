import json
from random import shuffle


class Functions():
    def isset(variable):
        """
        @asaenz
        Define si una variable esta creada o no. Si existe devuelve TRUE de lo contrario FALSE.
        :param variable:
        :return:
        """
        return variable in locals() or variable in globals()

    def handleJson(jsonPath):
        """
        @asaenz
        Manejar el objeto JSON del cual se cargan las preguntas. Devuelve un objeto con el contenido del archivo de source.
        :param jsonPath:
        :return:
        """

        # Se utiliza opne() para abrir el fichero JSON como texto plano. Los parámetros significan:
        # 'r' -> abrir en modo SOLO LECTURA
        # '-1' -> no crear Buffer
        # 'UTF-8' -> es la codificación del archivo.
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

