import easygui as eg


class Game:
    many = 10
    status = True

    def gameflow(player, questions):
        while Game.status is True:
            player.lap += 1
            cats = list()

            for category in questions:
                cats.append(category)

            msg = "Juego de: " + player.name
            msg += "\nCreditos: " + str(player.money)
            msg += "\n\nRonda: " + str(player.lap)
            msg += "\n"
            msg += "\nAciertos: " + str(player.right)
            msg += "\nErrores: " + str(player.mistakes)

            title = "Jeopardy SuperCool de ICC"
            choice = eg.choicebox(msg, title, cats)
            Game.showQuestion(questions, choice)
            Game.status = False
        return Game.status

    def showQuestion(questions, category):
        choices = list()
        for quest in questions[category]['preguntas']:
            if not quest['answered']:
                choices.append(quest['value'])

        image = category + ".gif"
        msg = "Selecciona el valor de una pregunta"
        reply = eg.buttonbox(msg, image=image, choices=choices)