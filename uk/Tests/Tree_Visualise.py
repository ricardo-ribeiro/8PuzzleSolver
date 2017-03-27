from pip._vendor.requests.packages.urllib3.connectionpool import xrange

__author__ = 'ricardo'
from treelib import Node, Tree
from uk.Algorithm.AStar_t import AStar_t
from uk.Heuristics.Manhattan import Manhattan
from uk.Heuristics.Nielssen import Nielssen
from uk.Heuristics.Out_Row_Column import Out_row_column
import json

class visualize:
    def __init__(self,ai_result):
        self.tree = Tree()
        self.tree_data = ai_result

    def view_node_tree(self):

        previous_node = "empty"
        previous_i = 0
        for i in xrange(len(self.tree_data)-1,0,-1):

            if i == len(self.tree_data)-1:
                self.tree.create_node(str(self.tree_data[i][0])+str(self.tree_data[i][1])+str(self.tree_data[i][2]), i )
            else:
                self.tree.create_node(str(self.tree_data[i][0])+str(self.tree_data[i][1])+str(self.tree_data[i][2]), i ,parent= previous_i )
            previous_node = self.tree_data[i]
            previous_i = i
        self.tree.create_node(str([[1,2,3], [8,0,4], [7, 6, 5]]), 0 ,parent= previous_i )

        self.tree.show()

    def view_board(self):
        print("\n Solution Steps: \n")
        for i in xrange(len(self.tree_data)-1,0,-1):

            print(str(self.tree_data[i][0])+"\n"+str(self.tree_data[i][1])+"\n"+str(self.tree_data[i][2])+"\n\t⬇")

        print(str([1,2,3])+"\n"+str([8,0,4])+"\n"+str([7, 6, 5]))

    def view_boardH(self):
        print("\n Solution Steps: \t Initial State -> Goal\n")
        for i in xrange(len(self.tree_data)-1,0,-1):
            print(str(self.tree_data[i][0])+"\t", end="")
        print(str([1,2,3]))
        for i in xrange(len(self.tree_data)-1,0,-1):
            print(str(self.tree_data[i][1])+"\t", end="")
        print(str([8,0,4]))
        for i in xrange(len(self.tree_data)-1,0,-1):
            print(str(self.tree_data[i][2])+"\t", end="")
        print(str([7, 6, 5]))

def logo():
        print("""   ,---.-,
  '   ,'  '.          ,-.----.
 /   /      \         \    /  \                                                ,--,                         .--.--.                 ,--,
.   ;  ,/.  :         |   :    \                                             ,--.'|                        /  /    '.             ,--.'|
'   |  | :  ;         |   |  .\ :          ,--,         ,----,        ,----, |  | :                       |  :  /`. /     ,---.   |  | :                            __  ,-.
'   |  ./   :         .   :  |: |        ,'_ /|       .'   .`|      .'   .`| :  : '                       ;  |  |--`     '   ,'\  :  : '         .---.            ,' ,'/ /|
|   :       ,         |   |   \ :   .--. |  | :    .'   .'  .'   .'   .'  .' |  ' |       ,---.           |  :  ;_      /   /   | |  ' |       /.  ./|    ,---.   '  | |' |
 \   \     /          |   : .   / ,'_ /| :  . |  ,---, '   ./  ,---, '   ./  '  | |      /     \           \  \    `.  .   ; ,. : '  | |     .-' . ' |   /     \  |  |   ,'
  ;   ,   '\          ;   | |`-'  |  ' | |  . .  ;   | .'  /   ;   | .'  /   |  | :     /    /  |           `----.   \ '   | |: : |  | :    /___/ \: |  /    /  | '  :  /
 /   /      \         |   | ;     |  | ' |  | |  `---' /  ;--, `---' /  ;--, '  : |__  .    ' / |           __ \  \  | '   | .; : '  : |__  .   \  ' . .    ' / | |  | '
.   ;  ,/.  :         :   ' |     :  | : ;  ; |    /  /  / .`|   /  /  / .`| |  | '.'| '   ;   /|          /  /`--'  / |   :    | |  | '.'|  \   \   ' '   ;   /| ;  : |
'   |  | :  ;         :   : :     '  :  `--'   \ ./__;     .'  ./__;     .'  ;  :    ; '   |  / |         '--'.     /   \   \  /  ;  :    ;   \   \    '   |  / | |  , ;
'   |  ./   :         |   | :     :  ,      .-./ ;   |  .'     ;   |  .'     |  ,   /  |   :    |           `--'---'     `----'   |  ,   /     \   \ | |   :    |  ---'
|   :      /          `---'.|      `--`----'     `---'         `---'          ---`-'    \   \  /                                   ---`-'       '---"   \   \  /
 \   \   .'             `---`                                                            `----'                                                          `----'
  `---`-'                                                                                                                                                                   """)

#nl = Nielssen([[1,2,3],[8,0,4],[7,6,5]])
#mh = Manhattan([[1,2,3],[8,0,4],[7,6,5]])
#out = Out_row_column([[1,2,3],[8,0,4],[7,6,5]])

#ast = AStar_t(mh,[[8,7,6],[2,0,3],[5,4,1]],[[1,2,3],[8,0,4],[7,6,5]])




#viz = visualize(ast.execute())
#viz.view_boardH()

print("")