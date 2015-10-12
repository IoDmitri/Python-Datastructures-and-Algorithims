from Digraph import Digraph
from Stack import Stack

class DirectedCycle:
	def __init__(self,digraph):
		self.marked = [False] * (digraph.v + 1)
		self.edgeTo = [None] * (digraph.v +1)
		self.cycle = None
		self.onStack = [False] * (digraph.v +1)

		for v in range(digraph.v +1):
			if self.marked[v] is False:
				self._dfs(digraph,v)

	def _dfs(self,dg,v):
		self.onStack[v] = True
		self.marked[v] = True
		for w in dg.adj(v):
			if (self.hasCycle()):
				return 
			elif (self.marked[w] is False):
				self.edgeTo[w] = v
				self._dfs(dg,w)
			elif(self.onStack[w]):
				self.cycle = Stack()
				x = self.edgeTo[v]
				while(x != w):
					self.cycle.push(x)
				self.cycle.push(w)
				self.cycle.push(v)

		self.onStack[v] = False

	def hasCycle(self):
		return self.cycle is not None


				
