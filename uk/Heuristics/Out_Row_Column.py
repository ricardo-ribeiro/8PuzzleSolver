__author__ = 'ricardo'

#### JUSTIN TO IMPLEMENT
#### RESULT SHOULD BE RETURNED ON CALCULATE FUNCTION
#### SO WE CAN CHANGE THE CLASS BUT HAVE SAME BEHAV..
class Out_row_column:
    def __init__(self,goalState):
        self.goalState = goalState
    def calculate(self,currentState):
        result = 0

        pattern = [[0,0],[0,1],[0,2],[1,2],[2,2],[2,1],[2,0],[1,0],[1,1]]
        expected = [[1],[2],[3],[4],[5],[6],[7],[8],[0]]
        outOfrow = 0
        outOfcolumn = 0
        for i in range(len(pattern)):
            xPos = self.getPosition(currentState,expected[i][0])[0]
            yPos = self.getPosition(currentState,expected[i][0])[1]
            if xPos[0] != pattern[i][0]:
                outOfrow += 1
            elif yPos[0] != pattern[i][1]:
                outOfcolumn +=1
        result = outOfrow + outOfcolumn
        return result

    def getPosition(self,currentState,value):
        for x in range(len(currentState[0])):
            for y in range(len(currentState[0])):
                if currentState[x][y] == value:
                    return [[x],[y]]


#out = Out_row_column([[1,2,3],[8,0,4],[7,6,5]])
#print(out.calculate([[2,1,3],[8,0,4],[7,6,5]]))
