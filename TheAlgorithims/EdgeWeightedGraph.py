from Edge import Edge
import os.path

class EdgeWeightedGraph:
	def __init__(self,v):
		#ToDo: implement constructing an EWG from a text file 
		if isinstance(v,file):
			pass
		else:
			pass
		self.v = v
		self.e = 0
		self._adj = []

		for x in range(v+1):
			self._adj.append([])


	def addEdge(self,e):
		v = e.either()
		w = e.other(v)
		self._adj[v].append(e)
		self._adj[w].append(e)
		self.e += 1

	def adj(self,v):
		return self._adj[v]

	def edges(self):
		edgs = []

		for v in range(self.v +1):
			for e in self._adj[v]:
				if (e.other(v)> v):
					edgs.append(e)
		return edgs

class EWGTest:
	def __init__(self):
		pass

	def testGraph(self):
		j = EdgeWeightedGraph(6)
		edges = []
		e1 = Edge(5,1,10)
		edges.append(e1)
		e2 = Edge(1,2,4)
		edges.append(e2)
		e3 = Edge(1,3,3)
		edges.append(e3)
		e4 = Edge(3,4,4)
		edges.append(e4)
		e5 = Edge(2,0,5)
		edges.append(e5)
		return j


