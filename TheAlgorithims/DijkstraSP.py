from EdgeWeightedDigraph import EdgeWeightedDigraph
from IndexMinPQ import IndexMinPQ
from Stack import Stack 
from DirectedEdge import DirectedEdge
import sys
class DijkstraSP:

	def __init__(self,ewd,s):
		self.edgeTo = [None] * (ewd.v+1)
		self.distTo = range(ewd.v+1)
		self.pq = IndexMinPQ(ewd.v+1)

		for x in self.distTo:
			self.distTo[x] = sys.maxint
		self.distTo[s] = 0.0

		self.pq.insert(s,0.0)
		while not self.pq.isEmpty():
			self._relax(ewd,self.pq.delMin())

	def _relax(self,ewd,v):
		for e in ewd.adj(v):
			w = e.dest
			distToV = self.distTo[v] + e.weight
			if (self.distTo[w] > distToV):
				self.distTo[w] = distToV
				self.edgeTo[w] = e

				if (self.pq.contains(w)):
					self.pq.change(w,self.distTo[w])
				else:
					self.pq.insert(w,self.distTo[w])

	def hasPathTo(self,v):
		return self.distTo[v] < sys.maxint

	def pathTo(self,v):
		if not self.hasPathTo(v):
			return None

		paths = Stack()

		e = self.edgeTo[v]
		while (e is not None):
			paths.push(e)
			e = self.edgeTo[e.source]

		return paths

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










