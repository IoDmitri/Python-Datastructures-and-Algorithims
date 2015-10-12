from Graph import Graph 
from Queue import Queue

class BreadthFirstSearch:

	def __init__(self,graph,source):
		self.makred = [False] * (graph.v + 1)
		self.edgeTo = [None] * (graph.v +1)
		self.s = source
		self._bfs(graph,self.s)
		self.size = graph.v

	def _bfs(self,graph,s):
		q = Queue()
		self.makred[s] = True
		q.enqueue(s)

		while not q.isEmpty():
			v = q.dequeue()
			for w in graph.adj(v):
				if self.makred[w] is False:
					self.edgeTo[w] = v
					self.makred[w] = True
					q.enqueue(w)

	def hasPathTo(self,v):
		return self.makred[v] is True

	def pathTo(self,v):
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

z = BreadthFirstSearch(j,0)

print(z.hasPathTo(3))
print(z.pathTo(4))
print(z.pathTo(3))
