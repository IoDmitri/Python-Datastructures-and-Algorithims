from Queue import Queue
from MinPQ import MinPQ
from unionFind import UnionFind 
from EdgeWeightedGraph import EdgeWeightedGraph
from Edge import Edge 

#an algorithim that takes an edge weighted graph and finds the minimal spanning tree 
#that connects all verticies
class KruskalMST:
	def __init__(self,ewg):
		self._mst = Queue()
		self._pq = MinPQ(ewg.edges())
		self._uf = UnionFind(ewg.v+1)

		while not self._pq.isEmpty() and self._mst.size < ewg.v-1:
			#get minimum weighted ege on the PQ
			e = self._pq.dequeue()
			#get the first vertex
			v = e.either()
			#get the second 
			w = e.other(v)

			if (self._uf.connected(v,w)):
				continue 
			self._uf.union(v,w)
			self._mst.enqueue(e)

	def edges(self):
		return self._mst
