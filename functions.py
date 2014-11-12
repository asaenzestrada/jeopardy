# Functions module
import json


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
        jsonData = open(jsonPath).read()
        myJson = json.loads(jsonData)

        return myJson