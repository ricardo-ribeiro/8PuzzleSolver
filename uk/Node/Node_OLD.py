

__author__ = 'ricardo'
# Node is each Posibility to be checked
class Node:
    def __init__(self):
        self.parrentNode = None
        self.manhattan = 0
        self.nilsson   = 0
        self.otherheuristic = 0
        self.board = [[],[],[]]

    def setParentNode(self,node):
        self.parrentNode = node
    def setManhattan(self,value):
        self.manhattan = value
    def setNilsson(self,value):
        self.nilsson = value
    def setOtherheuristic(self,value):
        self.otherheuristic = value
    def setBoard(self,board):
        self.board = board
    def getParentNode(self):
        return self.parrentNode
    def getManhattan(self):
        return self.manhattan
    def getNilsson(self):
        return self.nilsson
    def getOtherheuristic(self):
        return self.otherheuristic
    def getBoard(self):
        return list(self.board)
    def getValuePosition(self,value):
        for x in range(len(self.getBoard())):
            for y in range(len(self.getBoard())):
                if self.getBoard()[x][y] == value:
                    return x,y

    def __lt__(self,other):
        return True

    def generateChilds(self):
        queue = []

        # NEEDS IMPROVEMENT
        if self.getValuePosition(0) == (0, 0):
            queue.append(self.down(self.getBoard()))
            queue.append(self.right(self.getBoard()))
        elif self.getValuePosition(0) == (0, 1):
            queue.append(self.down(self.getBoard()))
            queue.append(self.right(self.getBoard()))
            queue.append(self.left(self.getBoard()))
        elif self.getValuePosition(0) == (0, 2):
            queue.append(self.down(self.getBoard()))
            queue.append(self.right(self.getBoard()))
        elif self.getValuePosition(0) == (1, 0):
            queue.append(self.up(self.getBoard()))
            queue.append(self.down(self.getBoard()))
            queue.append(self.right(self.getBoard()))
        elif self.getValuePosition(0) == (1, 1):
            queue.append(self.up(self.getBoard()))
            queue.append(self.down(self.getBoard()))
            queue.append(self.right(self.getBoard()))
            queue.append(self.left(self.getBoard()))
        elif self.getValuePosition(0) == (1, 2):
            queue.append(self.up(self.getBoard()))
            queue.append(self.down(self.getBoard()))
            queue.append(self.left(self.getBoard()))
        elif self.getValuePosition(0) == (2, 0):
            queue.append(self.up(self.getBoard()))
            queue.append(self.right(self.getBoard()))
        elif self.getValuePosition(0) == (2, 1):
            queue.append(self.up(self.getBoard()))
            queue.append(self.right(self.getBoard()))
            queue.append(self.left(self.getBoard()))
        elif self.getValuePosition(0) == (2, 2):
           # node_1 = Node()
            #node_1.setParentNode(self)
            #result = self.up(list(self.getBoard()))
            #node_1.setBoard(result)
            #queue.append(node_1)
            node_1 = self.up(list(self.getBoard()))
            node_1.setParentNode(self)
            queue.append(node_1)

            node_2 = Node()
            node_2.setParentNode(self)
            result = self.left(list(self.getBoard()))
            node_2.setBoard(result)
            queue.append(node_2)
            #node.setBoard(node.up(node.getParentNode().getBoard()))
            #queue.append(list(node.getBoard()))
            #node.setParentNode(self)
            #node.setBoard(node.left(node.getParentNode().getBoard()))
            #queue.append(list(node.getBoard()))
            #print(node)
            #node = self
            #node.setBoard(node.up(list(node.getBoard())))
            #queue.append(node)
            #node = 0
            #node = Node()
            #node.setBoard(self.left(list(self.getBoard())))
            #queue.append(node)

        return queue

        #for x in range(len(queue.priorityQueue)):
         #   print(queue.priorityQueue[1])

    def up(self,board):
        upNode = Node()
        upNode.setBoard(list(board))

        #boardd = list(board)
        zeroPos = upNode.getValuePosition(0)
        zeroY = zeroPos.__getitem__(1)
        zeroX = zeroPos.__getitem__(0)
        upValue = upNode.getBoard()[zeroX-1][zeroY]
        newboard = upNode.getBoard()
        newboard[zeroX-1][zeroY] = 0
        newboard[zeroX][zeroY] = upValue
        upNode.setBoard(newboard)
        return upNode
    def down(self,boardx):
        boardd = list(boardx)
        zeroPos = self.getValuePosition(0)
        zeroY = zeroPos.__getitem__(1)
        zeroX = zeroPos.__getitem__(0)
        downValue = boardd[zeroX+1][zeroY]
        boardd[zeroX+1][zeroY] = 0
        boardd[zeroX][zeroY] = downValue
        return boardd
    def left(self,board):
        boardd = list(board)
        zeroPos = self.getValuePosition(0)
        zeroY = zeroPos.__getitem__(1)
        zeroX = zeroPos.__getitem__(0)
        leftValue = boardd[zeroX][zeroY-1]
        boardd[zeroX][zeroY-1] = 0
        boardd[zeroX][zeroY] = leftValue
        return boardd
    def right(self,boardx):
        boardd = list(boardx)
        zeroPos = self.getValuePosition(0)
        zeroY = zeroPos.__getitem__(1)
        zeroX = zeroPos.__getitem__(0)
        rigthValue = boardd[zeroX][zeroY+1]
        boardd[zeroX][zeroY+1] = 0
        boardd[zeroX][zeroY] = rigthValue
        return boardd

    def __str__(self):
        return "Board:\t"+str(self.getBoard())
    def __cmp__(self, other):
        return self.getBoard() < other.getBoard()


#test = Node()
#test.setBoard([[2,8,3],
             #  [0,1,4],
              # [7,6,5]])
#parent = Node()
#parent.setBoard([[1,0,3],
               # [8,2,4],
                #[7,6,5]])
#test.setParentNode(parent)
#print(test.getBoard())
#print(test.getValuePosition(0,[[0,2,3],[8,1,4],[7,6,5]]))
#test.generateChilds()

#print(test.getParentNode().getBoard())
