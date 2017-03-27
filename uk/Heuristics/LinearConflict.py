from uk.Heuristics.Manhattan import Manhattan

__author__ = 'ricardo'
class LinearConflict:
    def __init__(self,goalState,mh):
        self.linearConflict = 0
        self.goalState = goalState
        self.manhathan = mh

    def calculate(self,currentState):
        distance = 0

        distance += self.manhathan.calculate(currentState)
        row0 = [1,2,3]
        row1 = [8,0,4]
        row2 = [7,6,5]
        puzzle = [row0,row1,row2]
        #print (puzzle)
        for i in range(len(currentState)):
            for x in range(len(currentState)):
                if currentState[i][x] in puzzle[i]:

                    if self.getPosition(puzzle,currentState[i][x]):
                        print("cState",currentState[i][x])
                        print("sState",puzzle[i])
        return distance

    def getPosition(self,currentState,value):
        for x in range(0,len(currentState[0])):
            for y in range(0,len(currentState[0])):
                if currentState[x][y] == value:
                    return [[x],[y]]

# online Exples for manhattan distance --- testing if it calculates the same given values.
#man = Manhattan([[1,2,3],[8,0,4],[7,6,5]])
#lc = LinearConflict([[1,2,3],[8,0,4],[7,6,5]],man)
#if(man.calculate([[7,2,4],[5,0,6],[8,3,1]]) == 18):
#    print("Test Pass")

#man = Manhattan([[1,2,3],[4,5,6],[7,8,0]])
#if(man.calculate([[8,1,3],[4,0,2],[7,6,5]]) == 10):
#    print("Test Pass")


#print(lc.calculate([[1,5,0],[6,7,4],[2,3,8]]))