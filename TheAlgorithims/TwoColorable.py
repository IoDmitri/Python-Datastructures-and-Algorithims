from Graph import Graph

class TwoColor:
	def __init__(self,graph):
		self.marked = [False] * (graph.v+1)
		self.isTwoColorable = True
		self.color = [False] * (graph.v+1)

		for x in range(graph.v +1):
			if self.marked[x] is False:
				self._dfs(graph,x)

	def _dfs(self,graph,v):
		self.marked[v] = True

		for w in graph.adj(v):
			if self.marked[w] is False:
				self.color[w] = not self.color[v]
				self._dfs(graph,w)
			elif self.color[w] == self.color[v]:
				self.isTwoColorable = False


j = Graph(6)
j.addEdge(1,2)
j.addEdge(1,3)
j.addEdge(0,2)
j.addEdge(5,1)
j.addEdge(3,4)
j.addEdge(0,4)
#j.addEdge(3,4)
#j.addEdge(0,4)

z = TwoColor(j)
print(z.isTwoColorable)