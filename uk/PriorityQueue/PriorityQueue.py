from _bisect import insort
from uk.Node.Node_OLD import Node

__author__ = 'ricardo'

from heapq import heappush, heappop

class PriorityQueue:
    def __init__(self):
        # Init method -- Constructor, Create a Array to old the values
        self.priorityQueue = []
    # Push the tuple to the List
    def push(self,tuple):

        heappush(self.priorityQueue,tuple)
    # Pop return the smalles value in the List
    def pop(self):
        return heappop(self.priorityQueue)[1]


#pq = PriorityQueue()
#nd = Node()
#nd.setBoard([[1,2,3],[8,0,4],[7,6,5]])
#pq.push((1,nd))
#nd = Node()
#nd.setBoard([[1,2,3],[8,0,4],[7,6,5]])
#pq.push((1,nd))
#nd = Node()
#nd.setBoard([[1,2,3],[8,0,4],[7,6,5]])
#pq.push((2,nd))
#print(pq.priorityQueue)
#print(pq.pop().getBoard())