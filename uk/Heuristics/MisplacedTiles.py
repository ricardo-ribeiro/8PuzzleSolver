__author__ = 'ricardo'


class MisplacedTiles:
    def __init__(self,goalState):
        self.misplacedTiles = 0
        self.goalState = goalState


    def calculate(self,currentState):
        distance = 0
        for i in range(len(currentState)):
            for x in range(len(currentState)):
                if currentState[i][x] !=  self.goalState[i][x]:
                    distance += 1


        return distance

