from uk.Heuristics.Manhattan import Manhattan

__author__ = 'ricardo'

#### JUSTIN TO IMPLEMENT
#### RESULT SHOULD BE RETURNED ON CALCULATE FUNCTION
#### SO WE CAN CHANGE THE CLASS BUT HAVE SAME BEHAV..
class Nielssen:
    def __init__(self,goalState):
        self.manhathan = Manhattan(goalState)
        self.nielssen = 0
        self.goalState = goalState
    def calculate(self,currentState):
        current_manhathan = self.manhathan.calculate(currentState)
        nielsson = 0

        # nielson = manhathan + 3*(s(n))
        # s(n) = sequence score = check arround the center in turn +2 every tile not following the proper sucessor and +1 if the center is not empty

        pattern = [[0,0],[0,1],[0,2],[1,2],[2,2],[2,1],[2,0],[1,0],[1,1]]

        expected = [[1],[2],[3],[4],[5],[6],[7],[8],[0]]
        #123
        #804
        #765
        sum =0
        for x in range(len(pattern) - 1):
            #print(currentState[pattern[x][0]][pattern[x][1]])
            #print("x",x)
            if currentState[pattern[x][0]][pattern[x][1]] != expected[x+1]:
                sum += 2
        if currentState[1][1] != expected[8]:
            sum += 1

        #print(sum)
        nielsson = current_manhathan + 3 * sum



        #print(nielsson)
        return nielsson

    def getPosition(self,currentState,value):
        for x in range(len(currentState[0])):
            for y in range(len(currentState[0])):
                if currentState[x][y] == value:
                    return [[x],[y]]


#nls = Nielssen([[1,2,3],[8,0,4],[7,6,5]])
#print(nls.calculate([[8,7,6],[1,0,5],[2,3,4]]))
