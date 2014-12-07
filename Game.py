import json


class Game:
    many = 10
    Status = True
    quest = {}
    def GameFlow(player, questions):
        while Game.Status is True:
            Game.printQuestionsBoard(questions)
            Game.Status = False
        return Game.Status


    def printQuestionsBoard(questionObj):
        cat = questionObj['q']
        file = "_________________________________________________________________"
        file += "____________________________________________\n\n"
        counter = 0

        #TODO: Change counter var by the name of the category.
        for category in cat:
            file += "|  " + category['Categoria'] + "   "
            for questions in range(len(category['preguntas'])):
                Game.quest[counter] = category['preguntas']
            counter += 1
        Break = "\n_______________________________________________________________"
        Break += "______________________________________________\n"

        file += "|" + Break

        result = {}
        resultIndex = 0

        for x in range(len(cat) - 1):
            for i in (range(Game.many -1)):
                result[x][i] = cat[x]['preguntas'][i]



        print(result)

        print('Hay ' + str(len(Game.quest)) + ' categorias')

        print('Hay ' + str(len(Game.quest[9]))  + ' Preguntas')

        # Group questions by category. ↓





        print(file)