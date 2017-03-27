__author__ = 'ricardo'
class Manhattan:
    def __init__(self,goalState):
        self.manhattan = 0
        self.goalState = goalState
    def calculate(self,currentState):
        distance = 0
        for x in range(3):
            for y in range(3):
                if(currentState[x][y] != 0):
                    positionInCurrent = self.getPosition(currentState,currentState[x][y])
                    x1 = positionInCurrent[0][0]
                    y1 = positionInCurrent[1][0]
                  #  print("value",currentState[x][y],"currentPosition",positionInCurrent)

                    positionInGoal = self.getPosition(self.goalState,currentState[x][y])

                    x2 = positionInGoal[0][0]
                    y2 = positionInGoal[1][0]
                  #  print("value",currentState[x][y],"goalPosition",positionInGoal)

                    distance += abs(x1-x2) + abs(y1 - y2)
        return distance

    def getPosition(self,currentState,value):
        for x in range(len(currentState[0])):
            for y in range(len(currentState[0])):
                if currentState[x][y] == value:
                    return [[x],[y]]

# online Exples for manhattan distance --- testing if it calculates the same given values.
#man = Manhattan([[0,1,2],[3,4,5],[6,7,8]])
#if(man.calculate([[7,2,4],[5,0,6],[8,3,1]]) == 18):
#    print("Test Pass")

#man = Manhattan([[1,2,3],[4,5,6],[7,8,0]])
#if(man.calculate([[8,1,3],[4,0,2],[7,6,5]]) == 10):
#    print("Test Pass")

#man = Manhattan([[1,2,3],[8,0,4],[7,6,5]])
#print(man.calculate([[1,5,0],[6,7,4],[2,3,8]]))