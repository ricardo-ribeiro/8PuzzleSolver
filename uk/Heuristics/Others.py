__author__ = 'ricardo'
class Other:
    def __init__(self,manhathan,nielsson,out_of_row,goalState):
        self.other = 0
        self.goalState = goalState
        self.mh = manhathan
        self.nh = nielsson
        self.out = out_of_row

    def calculate(self,currentState):

        result = 0

        result = (self.mh.calculate(currentState) + self.nh.calculate(currentState) + self.out.calculate(currentState))/3.7

        return result

