from Graph import Graph
class CC:
	def __init__(self,graph):
		self.marked = [False] * (graph.v +1)
		self.count = 0
		self._id = [None] * (graph.v +1)

		for x in range(graph.v +1):
			if self.marked[x] is False:
				self._dfs(graph,x)
				self.count += 1

	def _dfs(self,graph,v):
		self.marked[v] = True
		self._id[v] = self.count
		for w in graph.adj(v):
			if self.marked[w] is False:
				self._dfs(graph,w)

	def connected(self,v,w):
		return self._id[v] == self._id[w]

	def id(self,v):
		return self._id[v]

j = Graph(6)
j.addEdge(1,2)
j.addEdge(1,3)
j.addEdge(0,2)
j.addEdge(5,1)
j.addEdge(3,4)
j.addEdge(0,4)

z = CC(j)

print(z.connected(1,0))
print(z.id(6))


