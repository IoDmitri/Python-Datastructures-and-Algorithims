from DirectedEdge import DirectedEdge

class EdgeWeightedDigraph:

	def __init__(self,v):
		self.v = v
		self.e = 0
		self._adj = []

		for x in range(v+1):
			self._adj.append([])

	def addEdge(self,e):
		if not isinstance(e,DirectedEdge):
			raise ValueError('Provided argument is not a directed Edge')

		self._adj[e.source].append(e)
		self.e += 1

	def adj(self,v):
		return self._adj[v]

	def edges(self):
		edges = []

		for v in range(self.v+1):
			for e in self._adj[v]:
				edges.append(e)

		return edges



j = EdgeWeightedDigraph(6)
e1 = DirectedEdge(5,1,10)
j.addEdge(e1)
e2 = DirectedEdge(1,2,4)
j.addEdge(e2)
e3 = DirectedEdge(1,3,3)
j.addEdge(e3)
e4 = DirectedEdge(3,4,4)
j.addEdge(e4)
e5 = DirectedEdge(2,0,5)
j.addEdge(e5)
e6 = DirectedEdge(0,4,4)
j.addEdge(e6)




