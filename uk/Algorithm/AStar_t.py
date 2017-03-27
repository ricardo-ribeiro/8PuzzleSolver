from uk.Node.Node_t import Node_t

__author__ = 'ricardo'
from uk.Heuristics.Manhattan import Manhattan
from uk.Node.Node import Node
from uk.PriorityQueue.PriorityQueue import PriorityQueue
import time


class AStar_t:

    def __init__(self,heuristic,initialState,goalState,optimal):
        self.heuristic = heuristic
        self.initialState = list(initialState)
        self.goalState = goalState
        self.closedList = []
        self.start_time = time.time()
        self.movements=[]
        self.optimal = optimal
        self.openList = PriorityQueue()





    def execute(self):
        print("\n\n\nSolving in Progress! Do not exit this instance!\n\n")
        # Creating a Node Initial State:: Copy the initial state to the object node

        initialState = Node_t()
        initialState.setBoard(self.initialState)

        #print("Initial State:\t\t",initialState.getBoard())
        # Creating the Priority Queue OpenList


        # Adding the initial state to the openList
        # 0 is the initial cost: it can be 0 since its the initial state
        self.openList.push((0,initialState))
        count = 0
        fcost = 0
        moves = 0
        generatedNodes = 0
        currentNode = 0
        steps = []
        while len(self.openList.priorityQueue) != 0:

            previousNode = currentNode


            # Pop the node with the smaller heuristic value
            currentNode = self.openList.pop()
            #print(currentNode)


            # Testing if the current node is the solution

            if currentNode.compare(self.goalState) == 9:
                #print("------------------ Solution Found :) --------------------")
                reading_node = currentNode
                steps.append(currentNode.getBoard())
                for x in range(count):
                    if(reading_node == None):
                        break
                    if(reading_node != None):
                        reading_node = reading_node.getParentNode()
                        moves += 1
                    if(reading_node != None):
                        steps.append(reading_node.getBoard())
                        self.movements.append(reading_node.getDirection())

                #return {"solution":True,
                    #     "initial_state":initialState.getBoard(),
                     #    "n_moves":moves,
                      #   "t_nodes":count,
                       #  "g_nodes":generatedNodes,
                        # "cpu_time":time.time()-self.start_time,
                         #"solution_steps":steps,
                         #"solution_direction": self.movements}

                print(bcolors.WARNING+"Solution Moves : "+str(moves)+" \t Tested Nodes: "+str(count)+" \t Generated Nodes: ",str(generatedNodes))
                print(bcolors.FAIL+"CPU Time = ",time.time()-self.start_time)," s"
                print(bcolors.OKBLUE, end="")
                return steps


            #print("Current Test Node:\t",currentNode.getBoard())
            # Cupute the list of childs [ Node(),Node(),Node() ]
            child_list = currentNode.generateChilds()
            generatedNodes += len(child_list)

            good_to_add = list()

            # Analysing Child Nodes If they are already checked
            for i in range(len(child_list)):
                node_to_add = child_list[i]
                good_to_add = []

                for i in range(len(self.closedList)):
                    if node_to_add.compare(self.closedList[i].getBoard()) != 9:
                        good_to_add.append(True)
                    else:
                        good_to_add.append(False)

                for i in range(len(self.openList.priorityQueue) - 1):
                    if node_to_add.compare(self.openList.priorityQueue[i][1].getBoard()) != 9:
                        good_to_add.append(True)
                    else:
                        good_to_add.append(False)

                # 0 on the initial node
                node_to_add.setGcost(currentNode.getGcost() + 1)
                node_to_add_fn = node_to_add.getGcost() + self.heuristic.calculate(node_to_add.getBoard())
                node_to_add.setFcost(node_to_add_fn)

                if len(self.closedList) == 0 or all(good_to_add):
                    self.openList.push((node_to_add_fn,node_to_add))

            count += 1
            self.closedList.append(currentNode)



class bcolors:
    HEADER      =  '\033[95m'
    OKBLUE      =  '\033[94m'
    OKGREEN     = '\033[92m'
    WARNING     = '\033[93m'
    FAIL        =    '\033[91m'
    ENDC        = '\033[0m'
    BOLD        = '\033[1m'
    UNDERLINE   = '\033[4m'



