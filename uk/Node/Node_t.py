__author__ = 'ricardo'
__author__ = 'ricardo'
# Node is each Posibility to be checked
class Node_t:
    def __init__(self):
        self.parrentNode = None
        self.Fcost = 0
        self.manhattan = 0
        self.nilsson   = 0
        self.otherheuristic = 0
        self.board = [[],[],[]]
        self.direction = None
        self.Gcost = 0
    def getGcost(self):
        return self.Gcost
    def setGcost(self,gcost):
        self.Gcost = gcost
    def getFcost(self):
        return self.Fcost
    def setFcost(self,fcost):
        self.Fcost = fcost
    def getDirection(self):
        return self.direction
    def setDirection(self,dir):
        self.direction = dir
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
            for y in range(len(self.getBoard()[x])):
                if self.getBoard()[x][y] == value:
                    return x,y

    def __lt__(self,other):
        return True

    def generateChilds(self):
        queue = []
        loc = self.getValuePosition(0);

        # NEEDS IMPROVEMENT
        if loc == (0, 0):
            node_1 = self.down(self.getBoard())
            node_1.setParentNode(self)
            node_1.direction = "down"
            queue.append(node_1)

            node_2 = self.right(self.getBoard())
            node_2.setParentNode(self)
            node_2.direction = "right"
            queue.append(node_2)

        elif loc == (0, 1):
            node_1 = self.down(self.getBoard())
            node_1.setParentNode(self)
            node_1.direction = "down"
            queue.append(node_1)

            node_2 = self.left(self.getBoard())
            node_2.setParentNode(self)
            node_2.direction = "left"
            queue.append(node_2)

            node_3 = self.right(self.getBoard())
            node_3.setParentNode(self)
            node_3.direction = "right"
            queue.append(node_3)

        elif loc == (0, 2):
            node_1 = self.down(self.getBoard())
            node_1.setParentNode(self)
            node_1.direction = "down"
            queue.append(node_1)

            node_2 = self.left(self.getBoard())
            node_2.setParentNode(self)
            node_2.direction = "left"
            queue.append(node_2)

        elif loc == (1, 0):
            node_1 = self.up(self.getBoard())
            node_1.setParentNode(self)
            node_1.direction = "up"
            queue.append(node_1)

            node_2 = self.down(self.getBoard())
            node_2.setParentNode(self)
            node_2.direction = "down"
            queue.append(node_2)

            node_3 = self.right(self.getBoard())
            node_3.setParentNode(self)
            node_3.direction = "right"
            queue.append(node_3)

        elif loc == (1, 1):

            node_1 = self.up(self.getBoard())
            node_1.setParentNode(self)
            node_1.direction = "up"
            queue.append(node_1)

            node_2 = self.down(self.getBoard())
            node_2.setParentNode(self)
            node_2.direction = "down"
            queue.append(node_2)

            node_3 = self.right(self.getBoard())
            node_3.setParentNode(self)
            node_3.direction = "right"
            queue.append(node_3)

            node_4 = self.left(self.getBoard())
            node_4.setParentNode(self)
            node_4.direction = "left"
            queue.append(node_4)


        elif loc == (1, 2):

            node_1 = self.up(self.getBoard())
            node_1.setParentNode(self)
            node_1.direction = "up"
            queue.append(node_1)

            node_2 = self.down(self.getBoard())
            node_2.setParentNode(self)
            node_2.direction = "down"
            queue.append(node_2)

            node_3 = self.left(self.getBoard())
            node_3.setParentNode(self)
            node_3.direction = "left"
            queue.append(node_3)

        elif loc == (2, 0):
            node_1 = self.up(self.getBoard())
            node_1.setParentNode(self)
            node_1.direction = "up"
            queue.append(node_1)

            node_2 = self.right(self.getBoard())
            node_2.setParentNode(self)
            node_2.direction = "right"
            queue.append(node_2)

        elif loc == (2, 1):
            node_1 = self.up(self.getBoard())
            node_1.setParentNode(self)
            node_1.direction = "up"
            queue.append(node_1)

            node_2 = self.right(self.getBoard())
            node_2.setParentNode(self)
            node_2.direction = "right"
            queue.append(node_2)

            node_3 = self.left(self.getBoard())
            node_3.setParentNode(self)
            node_3.direction = "left"
            queue.append(node_3)

        elif loc == (2, 2):

            node_1 = self.up(self.getBoard())
            node_1.setParentNode(self)
            node_1.direction = "up"
            queue.append(node_1)

            node_2 = self.left(self.getBoard())
            node_2.setParentNode(self)
            node_2.direction = "left"
            queue.append(node_2)

        return queue

    def compare(self,node_to_compare):
        truth = 0 ;
        for x in range(len(self.getBoard())):
            for y in range(len(self.getBoard())):
                if self.getBoard()[x][y] == node_to_compare[x][y]:
                    truth += 1
        return truth

    def up(self,board):

        jNewBoard = self.copy_board(board)

        upNode = Node_t()
        upNode.setBoard(jNewBoard)

        zeroPos = upNode.getValuePosition(0)
        zeroY = zeroPos[1]
        zeroX = zeroPos[0]
        upValue = upNode.getBoard()[zeroX-1][zeroY]
        newboard = upNode.getBoard()
        newboard[zeroX-1][zeroY] = 0
        newboard[zeroX][zeroY] = upValue
        upNode.setBoard(newboard)
        return upNode

    def down(self,board):
        jNewBoard = self.copy_board(board)
        node = Node_t()
        node.setBoard(jNewBoard)
        zeroPos = node.getValuePosition(0)
        zeroY = zeroPos.__getitem__(1)
        zeroX = zeroPos.__getitem__(0)
        downValue = node.getBoard()[zeroX+1][zeroY]
        jNewBoard[zeroX+1][zeroY] = 0
        jNewBoard[zeroX][zeroY] = downValue
        node.setBoard(jNewBoard)
        return node

    def left(self,board):

        boardd = self.copy_board(board)
        node = Node_t()
        node.setBoard(boardd)

        zeroPos = node.getValuePosition(0)
        zeroY = zeroPos.__getitem__(1)
        zeroX = zeroPos.__getitem__(0)
        leftValue = node.getBoard()[zeroX][zeroY-1]
        boardd[zeroX][zeroY-1] = 0
        boardd[zeroX][zeroY] = leftValue
        node.setBoard(list(boardd))
        return node

    def right(self,board):

        boardd = self.copy_board(board)
        node = Node_t()
        node.setBoard(boardd)

        zeroPos = node.getValuePosition(0)
        zeroY = zeroPos.__getitem__(1)
        zeroX = zeroPos.__getitem__(0)
        rigthValue = node.getBoard()[zeroX][zeroY+1]
        boardd[zeroX][zeroY+1] = 0
        boardd[zeroX][zeroY] = rigthValue
        node.setBoard(boardd)
        return node

    def __str__(self):
        return "Board:\t"+str(self.getBoard())
    def __cmp__(self, other):
        return self.getBoard() < other.getBoard()

    def copy_board(self,board):
        jNewBoard = [[0,0,0],[0,0,0],[0,0,0]]
        for dirX in range(len(board)):
            for dirY in range(len(board[dirX])):
                jNewBoard[dirX][dirY] = board[dirX][dirY]
        return jNewBoard


#test = Node_t()
#test.setBoard([[2,8,3],
             #  [0,1,4],
              # [7,6,5]])
#parent = Node_t()
#parent.setBoard([[1,0,3],
               # [8,2,4],
                #[7,6,5]])
#test.setParentNode(parent)
#print(test.getBoard())
#print(test.getValuePosition(0,[[0,2,3],[8,1,4],[7,6,5]]))
#test.generateChilds()

#print(test.getParentNode()_t.getBoard())
