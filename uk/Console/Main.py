from uk.Algorithm.AStar import AStar
from uk.Heuristics.Manhattan import Manhattan


__author__ = 'ricardo'


def init():

    # Defining Heuristc Manhathan object giving a goal state
    mh  = Manhattan([[1,2,3],[8,0,4],[7,6,5]])
    #Creating an Astar object parsin the heuristic the initial state and the goal state
    #--- heuristic must implement method calculate so you can define any object heuristic
    star = AStar(mh,[[0,2,3],[1,8,4],[7,6,5]],[[1,2,3],[8,0,4],[7,6,5]])
    star.execute()

init()