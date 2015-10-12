#class for a directed graph
class Digraph:
	def __init__(self,v):
		#verticies
		self.v = v
		#edges
		self.e = 0
		self._adj = []

		for x in range(v+1):
			self._adj.append([])


	def addEdge(self,v,w):
		#add w to v's adjecency list
		self._adj[v].append(w)
		#increment the number of edges within this particular graph
		self.e+= 1

	def adj(self,v):
		return self._adj[v]

	def reverse(self):
		r = Digraph(self.v)
		for v in range(self.v+1):
			for w in self._adj[v]:
				r.addEdge(w,v)
		return r


