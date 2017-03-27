from uk.Algorithm.AStar import AStar
from uk.Algorithm.AStar_t import AStar_t
from uk.Heuristics.LinearConflict import LinearConflict
from uk.Heuristics.Manhattan import Manhattan
from uk.Heuristics.MisplacedTiles import MisplacedTiles
from uk.Heuristics.Nielssen import Nielssen
from uk.Heuristics.Others import Other
from uk.Heuristics.Out_Row_Column import Out_row_column
from uk.Tests.Tree_Visualise import visualize
from uk.Tests.Tree_Visualise import logo

__author__ = 'ricardo'


GOALSTATE = [[1,2,3],[8,0,4],[7,6,5]]

INITIALSTATE = [[0,7,6],[8,2,4],[5,1,3]]

# Purposed Boards
#
#   2 -   [[8,7,6],[1,0,5],[2,3,4]]
#   5 -   [[6,0,3],[8,2,7],[5,4,1]]
#   10 - [[8,7,3],[0,6,5],[4,2,1]]
#   16 - [[7,6,3],[0,4,2],[8,5,1]]
#   17 - [[0,7,6],[8,2,4],[5,1,3]]
#   22 - [[8,6,0],[4,7,3],[2,5,1]]
#   24 - [[8,0,3],[4,6,1],[2,7,5]]
#   25 - [[2,8,6],[7,0,3],[5,4,1]]
#   26 - [[5,8,6],[0,7,3],[4,2,1]]
#   29 - [[7,6,3],[0,8,4],[2,5,1]]
#

## Heuristic Initialisation
## Parsing the Defined Goal State

nl = Nielssen(GOALSTATE)
mh = Manhattan(GOALSTATE)
out = Out_row_column(GOALSTATE)
oth = Other(mh,nl,out,GOALSTATE)
lc = LinearConflict(GOALSTATE,mh)
mt = MisplacedTiles(GOALSTATE)

HEURISTIC = oth


# Print 8Puzzle Logo
logo()
# Create Object Astar Parsing the Heuristic Object the Initial State the Goal State and the Optimal variable
ast = AStar_t(HEURISTIC,INITIALSTATE,GOALSTATE,True)
# The Viz Object provides diferrent display method for the rusult
# Create a visualize Object parsing the return value of the ast.execute method
viz = visualize(ast.execute())

# View Horizontal Board
viz.view_boardH()

