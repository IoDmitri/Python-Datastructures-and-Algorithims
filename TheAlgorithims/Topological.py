from Digraph import Digraph
from DepthFirstOrder import DepthFirstOrder
from DigraphCycle import DirectedCycle

class Topological:
	def __init__(self,digraph):
		self._order = None
		cycleFinder = DirectedCycle(digraph)
		if not cycleFinder.hasCycle():
			dfs = DepthFirstOrder(digraph)
			self._order = dfs.reversePost

	#Directed Acyclical Graph: A graph with no cycles 
	def isDAG(self):
		return self._order is not None

	def order(self):
		return self._order


j = Digraph(6)
j.addEdge(1,2)
j.addEdge(1,3)
j.addEdge(0,2)
j.addEdge(5,1)
j.addEdge(3,4)
j.addEdge(0,4)

z = Topological(j)
print(z.isDAG())

