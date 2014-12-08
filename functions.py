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
        Manejar el objeto JSON del cual se cargan las preguntas. Devuelve un objeto con el contenido del archivo de source.

        @asaenz
        :param jsonPath:
        :return:
        """

        # Se utiliza opne() para abrir el fichero JSON como texto plano. Los parámetros significan:
        # 'r' -> abrir en modo SOLO LECTURA
        # '-1' -> no crear Buffer
        # 'UTF-8' -> es la codificación del archivo.
        jsonData = open(jsonPath, 'r', -1, 'UTF-8').read()
        myJson = json.loads(jsonData)
        #Functions.assignValues(myJson)

        print(myJson)
        return myJson

    def assignValues(QJson):
        now = 0
        value = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
        shuffle(value)  # Reordenar aleatoriamente.

        for cat in QJson['q']:
            for quest in cat:
                if now > len(value):
                    break
                quest['value'] = value[now]
                now += 1