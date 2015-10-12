from Graph import Graph 

#DepthFirstSearch class that takes in a graph, and a start point
#the class finds all of the connects between the start point and all other
#verticies within the graph 

class DepthFirstSearch:
	def __init__(self,graph,source):
		assert isinstance(graph,Graph)
		#track the visisted nodes
		self.marked = [False] * (graph.v + 1)
		#Tracks from which edge was a vertex visisted from
		self.edgeTo = [None] * (graph.v +1)
		#the source that the process starts from
		self.s = source
		#size of the graph
		self.size = graph.v
		#call to DFS to start the process
		self._dfs(graph,self.s)

	def _dfs(self,graph,v):
		#mark w as visited
		self.marked[v] = True
		for w in graph.adj(v):
			#continue to DFS only if w is unmarked
			if self.marked[w] is False:
				self.edgeTo[w] = v
				self._dfs(graph,w)

	def hasPathTo(self,v):
		return self.marked[v] is not None

	def pathTo(self,v):
		#only in API for undirected graphs
		if v >self.size or not (self.hasPathTo(v)) or self.edgeTo[v] is None:
			return None 

		paths = []
		x = v
		while(x != self.s):
			paths.append(x)
			x = self.edgeTo[x]
		paths.append(self.s)
		return paths


j = Graph(6)
j.addEdge(1,2)
j.addEdge(1,3)
j.addEdge(0,2)
j.addEdge(5,1)
j.addEdge(3,4)
j.addEdge(0,4)

z = DepthFirstSearch(j,0)

print(z.hasPathTo(3))
print(z.pathTo(4))
print(z.pathTo(5))



