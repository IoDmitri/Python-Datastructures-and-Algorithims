from Digraph import Digraph
from DepthFirstOrder import DepthFirstOrder

class KosarajuSCC:
	def __init__(self,digraph):
		#number of verticies within the graph
		v = digraph.v +1
		self.marked = [False] * v
		self.id = [None] * v
		self.count = 0
		order = DepthFirstOrder(digraph.reverse())
		for s in order.reversePost():
			print(s)
			if self.marked[s] is False:
				self._dfs(digraph,s)
				self.count += 1

	def _dfs(self,digraph,v):
		self.marked[v] = True
		self.id[v] = self.count
		for w in digraph.adj(v):
			if self.marked[w] is False:
				self._dfs(digraph,w)

	def stronglyConnected(self,v,w):
		print("id of V:",self.id[v])
		print("id of W:",self.id[w])
		return self.id[v] == self.id[w]


j = Digraph(6)
j.addEdge(1,2)
j.addEdge(1,3)
j.addEdge(0,2)
j.addEdge(5,1)
j.addEdge(3,4)
j.addEdge(0,4)

z = KosarajuSCC(j)
print(z.stronglyConnected(3,4))

for x in z.id:
	print(x)