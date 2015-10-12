from Graph import Graph

class Cycle:
	def __init__(self,graph):
		self.marked = [False] * (graph.v + 1)
		self.hasCycle = False

		for x in range(graph.v+1):
			if self.marked[x] is False:
				self._dfs(graph,x,x)

	def _dfs(self,graph,v,u):
		self.marked[v] = True
		for w in graph.adj(v):
			if self.marked[w] is False:
				self._dfs(graph,w,v)
			elif w != u:
				self.hasCycle = True

j = Graph(6)
j.addEdge(0,1)
j.addEdge(1,2)
j.addEdge(2,3)
j.addEdge(3,4)
#j.addEdge(3,4)
#j.addEdge(0,4)

z = Cycle(j)
print(z.hasCycle)