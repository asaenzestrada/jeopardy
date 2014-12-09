import easygui as eg
import sys


class Player:
    name = ""
    money = 500
    right = 0
    mistakes = 0
    lap = 0

    def createUser(self=True):
        msg = "Dame tu nombrecillo"
        title = "Nombresillo"
        fieldNames = ["Name"]
        fieldValues = []  # we start with blanks for the values
        fieldValues = eg.multenterbox(msg, title, fieldNames)

        try:
            res = fieldValues[0]
        except Exception:
            sys.exit()

        Player.name = res
        return True