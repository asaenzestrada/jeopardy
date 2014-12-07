import functions
import player
import Game


questions = functions.Functions.handleJson('Assets/opciones.json')

player1 = player.Player
player1.createUser()

print("Bienvenido, " + player1.name + "\n Espero que estes listijirijillo para jugar!\n")

jeopardy = Game.Game.GameFlow(player1, questions)
