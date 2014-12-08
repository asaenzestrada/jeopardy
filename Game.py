import easygui as eg


class Game:
    many = 10
    status = True

    def gameflow(player, questions):
        while Game.status is True:
            player.lap += 1
            cats = list()

            for category in questions['q']:
                cats.append(category['Categoria'])

            msg = "Juego de: " + player.name
            msg += "\nCreditos: " + str(player.money)
            msg += "\n\nRonda: " + str(player.lap)
            msg += "\n"
            msg += "\nAciertos: " + str(player.right)
            msg += "\nErrores: " + str(player.mistakes)

            title = "Jeopardy SuperCool de ICC"
            choice = eg.choicebox(msg, title, cats)

            print(choice)

            Game.status = False
        return Game.status