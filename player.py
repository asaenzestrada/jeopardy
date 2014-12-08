import easygui as eg


class Player:
    name = ""
    money = 0
    right = 0
    mistakes = 0
    lap = 0

    def createUser(self=True):
        msg = "Dame tu nombrecillo"
        title = "Nombresillo"
        fieldNames = ["Name"]
        fieldValues = []  # we start with blanks for the values
        fieldValues = eg.multenterbox(msg, title, fieldNames)
        res = fieldValues[0]

        Player.name = res  # input("Dame tu nombresillo ;)\n")
        return True