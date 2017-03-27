from time import time
import heapq
from uk.ricardoribeiro.Heuristics.Manhattan import Manhattan
from uk.ricardoribeiro.Queue.QueuePriority import QueuePriority


__author__ = 'Ricardo Luis Ribeiro'




class Astar:

    openList = []
    closedList = []


    #openList = QueuePriority.prioritylist


    def __init__(self, initialState, goalState):
        self.initialState   = initialState
        self.goalState      = goalState
        # initialize number of iterations to 0 -- iteration count
        self.iterations = 0
        self.priorityQueue =  QueuePriority();

    def compare(self,l1,l2):
        pairwise = zip (l1, l2)
        matched_digits = [idx for idx, pair in enumerate(pairwise) if pair[0] == pair[1]]
        if len(matched_digits) == len(l1) and len(l2):
            return True
        return False



    def generateposiblemoves(self):
        self.counter += 1
        print("Processing: ",str(self.counter))
        if self.currentState[0] == 0:
            index1 = int(self.currentState[1])
            index3 = int(self.currentState[3])

            listOne = list(self.currentState)
            listOne[0] = index3
            listOne[3] = 0
            if not self.inClosedList(listOne):
                self.priorityQueue.push(listOne)
            #self.openList.append()

            list2 = list(self.currentState)
            list2[0] = index1
            list2[1] = 0
            if not self.inClosedList(list2):
                self.priorityQueue.push(list2)

        #BUG ON THIS ONE
        if self.currentState[1] == 0:

            #print(list(self.currentState))
            index0 = int(self.currentState[0])
            index2 = int(self.currentState[2])
            index4 = int(self.currentState[4])

            listOne = list(self.currentState)
            listOne[1] = index0
            listOne[0] = 0
            if not self.inClosedList(listOne):
                self.priorityQueue.push(listOne)

            list2 = list(self.currentState)
            list2[1] = index2
            list2[2] = 0
            if not self.inClosedList(list2):
                self.priorityQueue.push(list2)

            list3 = list(self.currentState)
            list3[1] = index4
            list3[4] = 0
            if not self.inClosedList(list3):
                self.priorityQueue.push(list3)

        if self.currentState[2] == 0:

            index1 = int(self.currentState[1])
            index5 = int(self.currentState[5])


            listOne = list(self.currentState)
            listOne[2] = index1
            listOne[1] = 0
            if not self.inClosedList(listOne):
                self.priorityQueue.push(listOne)

            list2 = list(self.currentState)
            list2[5] = index5
            list2[2] = 0
            if not self.inClosedList(list2):
                self.priorityQueue.push(list2)


        if self.currentState[3] == 0:

            index0 = int(self.currentState[0])
            index4 = int(self.currentState[4])
            index6 = int(self.currentState[6])

            listOne = list(self.currentState)
            listOne[3] = index0
            listOne[0] = 0
            if not self.inClosedList(listOne):
                self.priorityQueue.push(listOne)


            list2 = list(self.currentState)
            list2[3] = index4
            list2[4] = 0
            if not self.inClosedList(list2):
                self.priorityQueue.push(list2)


            list3 = list(self.currentState)
            list3[3] = index6
            list3[6] = 0
            if not self.inClosedList(list3):
                self.priorityQueue.push(list3)

        if self.currentState[4] == 0:

            index1 = int(self.currentState[1])
            index3 = int(self.currentState[3])
            index5 = int(self.currentState[5])
            index7 = int(self.currentState[7])

            listOne = list(self.currentState)
            listOne[4] = index1
            listOne[1] = 0
            if not self.inClosedList(listOne):
                self.priorityQueue.push(listOne)


            list2 = list(self.currentState)
            list2[4] = index3
            list2[3] = 0
            if not self.inClosedList(list2):
                self.priorityQueue.push(list2)


            list3 = list(self.currentState)
            list3[4] = index5
            list3[5] = 0
            if not self.inClosedList(list3):
                self.priorityQueue.push(list3)

            list4 = list(self.currentState)
            list4[4] = index7
            list4[7] = 0
            if not self.inClosedList(list4):
                self.priorityQueue.push(list4)

        if self.currentState[5] == 0:

            index2 = int(self.currentState[2])
            index4 = int(self.currentState[4])
            index8 = int(self.currentState[8])


            listOne = list(self.currentState)
            listOne[5] = index2
            listOne[2] = 0
            if not self.inClosedList(listOne):
                self.priorityQueue.push(listOne)


            list2 = list(self.currentState)
            list2[5] = index4
            list2[4] = 0
            if not self.inClosedList(list2):
                self.priorityQueue.push(list2)


            list3 = list(self.currentState)
            list3[5] = index8
            list3[8] = 0
            if not self.inClosedList(list3):
                self.priorityQueue.push(list3)

        if self.currentState[6] == 0:

            index3 = int(self.currentState[3])
            index7 = int(self.currentState[7])

            listOne = list(self.currentState)
            listOne[6] = index3
            listOne[3] = 0
            if not self.inClosedList(listOne):
                self.priorityQueue.push(listOne)


            list2 = list(self.currentState)
            list2[6] = index7
            list2[7] = 0
            if not self.inClosedList(list2):
                self.priorityQueue.push(list2)

        if self.currentState[7] == 0:

            index4 = int(self.currentState[4])
            index6 = int(self.currentState[6])
            index8 = int(self.currentState[8])

            listOne = list(self.currentState)
            listOne[7] = index4
            listOne[4] = 0
            if not self.inClosedList(listOne):
                self.priorityQueue.push(listOne)


            list2 = list(self.currentState)
            list2[7] = index6
            list2[6] = 0
            if not self.inClosedList(list2):
                self.priorityQueue.push(list2)

            list3 = list(self.currentState)
            list3[7] = index8
            list3[8] = 0
            if not self.inClosedList(list3):
                self.priorityQueue.push(list3)

        if self.currentState[8] == 0:

            index5 = int(self.currentState[5])
            index7 = int(self.currentState[7])


            listOne = list(self.currentState)
            listOne[8] = index5
            listOne[5] = 0
            if not self.inClosedList(listOne):
                self.priorityQueue.push(listOne)


            list2 = list(self.currentState)
            list2[8] = index7
            list2[7] = 0
            if not self.inClosedList(list2):
                self.priorityQueue.push(list2)





astar = Astar([1,6,3,
               8,2,4,
               7,0,5],[1,2,3,
                       8,0,4,
                       7,6,5])


print("Initial State:\t" + str(astar.initialState))
print("Goal State:\t\t" + str(astar.goalState))
print("Solution Path:\t" + str(astar.execute()))
print("Time Elapsed:\t" + str(astar.finishTime - astar.startedTime) + " s")

#del astar