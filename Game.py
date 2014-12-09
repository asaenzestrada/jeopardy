import easygui as eg
import functions

class Game:
    questions = functions.Functions.handleJson('Assets/opciones.json')
    many = 10
    status = True

    def gameflow(player):
        while Game.status is True:
            player.lap += 1
            cats = list()

            for category in Game.questions:
                cats.append(category)

            msg = "Juego de: " + player.name
            msg += "\nCreditos: " + str(player.money)
            msg += "\n\nRonda: " + str(player.lap)
            msg += "\n"
            msg += "\nAciertos: " + str(player.right)
            msg += "\nErrores: " + str(player.mistakes)

            title = "Jeopardy SuperCool de ICC"
            category = eg.choicebox(msg, title, cats)
            if not category:
                break
            choices = list()
            for quest in Game.questions[category]['preguntas']:
                if not quest['answered']:
                    choices.append(quest['value'])

            image = "Assets/imagenes/" + category + ".gif"
            msg = "Selecciona el valor que quieres ganar"
            chosen = eg.buttonbox(msg, image=image, choices=choices)

            for quest in Game.questions[category]['preguntas']:
                if not quest['answered'] and quest['value'] == chosen:
                    msg = quest['Pregunta']
                    options = list()
                    for option in quest['opciones']:
                        options.append(option['opcion'])
                        try:
                            Correcta = option['Correcta']
                            Correcta = option['opcion']
                        except KeyError:
                            pass
                    reply = eg.buttonbox(msg, image=image, choices=options)
                    quest['answered'] = True
                    if reply == Correcta:
                        eg.msgbox("Bien, por ahora...\n\nHaz ganado $" + str(quest['value']), ok_button="seguir...")
                        player.right += 1
                        player.money += quest['value']
                    else:
                        eg.msgbox("Incorrecto amiguito... que triste\nLa respuesta es:\n" + Correcta + "\n\nHaz perdido $100", ok_button="okaaaay :(");
                        player.mistakes += 1
                        player.money -= 100

                if player.mistakes > 5 or player.money < 0:
                    Game.status = False

        msg = "\nJuego de: " + player.name
        msg += "\nCreditos: " + str(player.money)
        msg += "\n\nRonda: " + str(player.lap)
        msg += "\n"
        msg += "\nAciertos: " + str(player.right)
        msg += "\nErrores: " + str(player.mistakes)

        if Game.status == False:
            eg.msgbox("Has perdido, este jeopardy es mucho para ti..." + msg, ok_button="byeeeee :(");
        eg.msgbox("Has Ganado, te mereces el respeto de un pythonista..." + msg, ok_button="Salir");
