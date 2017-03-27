from uk.Heuristics.Manhattan import Manhattan
from uk.Node.Node import Node
from uk.PriorityQueue.PriorityQueue import PriorityQueue
import time

__author__ = 'ricardo'

class AStar:

    def __init__(self,heuristic,initialState,goalState):
        self.heuristic = heuristic
        self.initialState = list(initialState)
        self.goalState = goalState
        self.closedList = []
        self.start_time = time.time()
        self.movements=[]

    def execute(self):
        # Creating a Node Initial State:: Copy the initial state to the object node

        initialState = Node()
        initialState.setBoard(self.initialState)

        print("Initial State:\t\t",initialState.getBoard())
        # Creating the Priority Queue OpenList
        openList = PriorityQueue()

        # Adding the initial state to the openList
        # 0 is the initial cost: it can be 0 since its the initial state
        openList.push((0,initialState))
        count = 0
        fcost = 0
        moves = 0

        steps = []
        while len(openList.priorityQueue) != 0:

            # Pop the node with the smaller heuristic value
            currentNode = openList.pop()
            for i in range(len(self.closedList)):
                if currentNode.compare(self.closedList[i].getBoard()) == 9:
                    #same
                    currentNode = openList.pop()
                    continue

            if currentNode.compare(self.goalState) == 9:
                print("------------------ Solution Found :) --------------------")
                reading_node = currentNode
                steps.append(currentNode.getBoard())
                print(currentNode)
                for x in range(count):
                    if(reading_node == None):
                        break
                    if(reading_node != None):
                        reading_node = reading_node.getParentNode()
                        moves += 1
                    if(reading_node != None):
                        print(reading_node)
                        steps.append(reading_node.getBoard())
                        self.movements.append(reading_node.getDirection())
                print("Total Number of Moves: ",moves)
                print("Tested Nodes: ",count)
                print("Computation Time: " ,time.time()-self.start_time," s")
                return [steps,self.movements]


            #print("Current Test Node:\t",currentNode.getBoard())
            # Cupute the list of childs [ Node(),Node(),Node() ]
            child_list = currentNode.generateChilds()
            # Analysing Child Nodes If they are already checked
            for i in range(len(child_list)):
                node_to_add = Node()
                node_to_add.setParentNode(currentNode)
                node_to_add.setBoard(child_list[i])
                
                #print("Adding this note to openList: ", node_to_add)
               # if node_to_add not in self.closedList:
                #    print("Node already Checked")
                 #   openList.push((self.heuristic.calculate(node_to_add.getBoard()),node_to_add))

                for x in range(len(self.closedList)):
                    if(currentNode.compare(node_to_add.getBoard()) == 9 ):
                       # print("already in list")
                        continue
                    if(self.closedList[x].compare(node_to_add.getBoard()) == 9 ):
                        #print("already in list")
                        continue
                    elif openList.priorityQueue[x][1].compare(node_to_add.getBoard()) == 9 :
                        #print("already in list")
                        continue
                    else:
                        openList.push((self.heuristic.calculate(node_to_add.getBoard()),node_to_add))
                        break
                if(self.closedList == []):
                    openList.push((self.heuristic.calculate(node_to_add.getBoard()),node_to_add))
            count += 1
            self.closedList.append(currentNode)




# Defining Heuristc Manhathan object giving a goal state
#mh  = Manhattan([[1,2,3],[8,0,4],[7,6,5]])
#Creating an Astar object parsin the heuristic the initial state and the goal state
#--- heuristic must implement method calculate so you can define any object heuristic
#star = AStar(mh,[[0,2,3],[1,8,4],[7,6,5]],[[1,2,3],[8,0,4],[7,6,5]])
#star.execute()