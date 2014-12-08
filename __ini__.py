from setuptools.command.easy_install import easy_install
import functions
import sys
import player
import Game

questions = functions.Functions.handleJson

player1 = player.Player
player1.createUser()

jeopardy = Game.Game.gameflow(player1, questions)
