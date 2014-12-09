import player
import Game
import easygui as eg


#Las instrucciones son dinamicas.
welcome = "Bienvenido al Jeopardy mas cool de ICC!"
welcome += "\n\n\nLas reglas son simples:\n"
welcome += "\n1.- Ganas llegando a " + str(Game.Game.GameLimit) + " rondas con menos de " + str(Game.Game.ErrorLimit) + " errores acumulados."
welcome += "\n2.- Ganaras el dinero que acumules. Comienzas el juego con: $" + str(player.Player.money) + "."
welcome += "\n3.- Cada respuesta incorrecta te hace perder $" + str(Game.Game.LooseMoney) + "."
welcome += "\n4.- Al comenzar el juego te pedira tu nombre."
welcome += "\n5.- Depues veras las categorias del juego, al elegir una se abrira la ventana que corresponde a esta categoria y "
welcome += "te mostrara el dinero que ganaras al responder esa pregunta. Debes seleccionar uno de los botones."
welcome += "\n6.- Depues se te mostrara la pregunta y las posibles respuestas, debes dar clic en el boton que contiene la que eliges."
welcome += "\n7.- Despes de seleccionar una respuesta se te indicara la respuesta correcta y el estado de tu juego y cartera en ese momento."
welcome += "\n8.- Si continuas en el juego se te mostraran de nuevo las categorias para continuar jugando."

eg.msgbox(welcome)

player1 = player.Player
player1.createUser()
jeopardy = Game.Game.gameflow(player1)
