import easygui as eg
import functions
from sys import exit
import random


class Game:
    questions = functions.Functions.handleJson('Assets/opciones.json')
    incorrectAnswers = [
        "Que va! juras que la contestaste mal!",
        "Incorrecto amiguito... que triste",
        "EEEEEEEERRRRRRRROOOOOOOOOORRRRRRR!!!!!!!",
        "Negativo, pareja",
        "Suerte a la proxima, cuate",
        "UUUY! te la encargo para la otra..."
    ]
    correctAnswers = [
        "Bien, por ahora...",
        "Dale, dale... Una buena",
        "Buen ritmo, eh",
        "Esa estuvo facil... Bien hecho",
        "SIgue asi, campeon",
        "ATTA BOY"
    ]

    status = True
    ErrorLimit = 5
    GameLimit = 30
    MoneyLimit = -1000
    LooseMoney = 100
    Win = False

    def gameflow(player):
        while Game.status is True:
            player.lap += 1
            cats = list()

            for category in Game.questions:
                cats.append(category)
            title = "Jeopardy SuperCool de ICC"
            category = eg.choicebox(Game.getMessage(player), title, cats)
            if not category:
                break
            choices = list()
            for quest in Game.questions[category]['preguntas']:
                if not quest['answered']:
                    choices.append(quest['value'])

            image = "Assets/imagenes/" + category + ".gif"
            msg = "Selecciona el valor que quieres ganar"
            if len(choices) > 0:
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
                    random.shuffle(options)
                    reply = eg.buttonbox(msg, image=image, choices=options)
                    quest['answered'] = True
                    if reply == Correcta:
                        eg.msgbox(random.choice(Game.correctAnswers) + "\n\nHaz ganado $" + str(quest['value']),
                                  ok_button="seguir...")
                        player.right += 1
                        player.money += quest['value']
                    else:
                        eg.msgbox(random.choice(Game.incorrectAnswers) + "\nLa respuesta es:\n"
                                  + Correcta + "\n\nHaz perdido $" + str(Game.LooseMoney), ok_button="okaaaay :(");
                        player.mistakes += 1
                        player.money -= Game.LooseMoney

                if player.mistakes > Game.ErrorLimit or player.money < Game.MoneyLimit:
                    Game.status = False
                    eg.msgbox("Has perdido, este jeopardy es mucho para ti...\n\n" + Game.getMessage(player),
                              ok_button="byeeeee :(")
                    exit()
                if player.lap > Game.GameLimit and player.money > Game.MoneyLimit and player.mistakes < Game.ErrorLimit:
                    Game.status = False
                    Game.Win = True
        if Game.Win:
            eg.msgbox("Has Ganado, te mereces el respeto de un pythonista...\ny te llevas $"
                      + str(player.money) + "\n" + Game.getMessage(player), ok_button="Salir")

    def getMessage(player):
        msg1 = "Juego de: " + player.name
        msg1 += "\nCreditos: " + str(player.money)
        msg1 += "\n\nRonda: " + str(player.lap)
        msg1 += "\n"
        msg1 += "\nAciertos: " + str(player.right)
        msg1 += "\nErrores: " + str(player.mistakes)
        return msg1