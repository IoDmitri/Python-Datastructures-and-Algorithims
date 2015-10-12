from Digraph import Digraph 
#Directed DFS for a digraph
class DirectedDFS:
	def __init__(self,graph,source):
		self.marked = [False] * (graph.v + 1)
		self._dfs(graph,source)

	def _dfs(self,g,v):
		self.marked[v] = True
		#itterate vertex v's adjecent nodes
		for w in g.adj(v):
			#DFS only on those elements who are unmarked
			if self.marked[w] is False:
				self._dfs(g,w)

	def hasPathTo(self,v):
		return self.marked[v]== True



j = Digraph(6)
j.addEdge(1,2)
j.addEdge(1,3)
j.addEdge(0,2)
j.addEdge(5,1)
j.addEdge(3,4)
j.addEdge(0,4)

z= DirectedDFS(j,1)
print(z.hasPathTo(3))




