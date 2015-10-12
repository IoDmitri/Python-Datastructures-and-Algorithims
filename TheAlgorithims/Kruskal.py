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

j = EdgeWeightedGraph(6)
e1 = Edge(5,1,10)
j.addEdge(e1)
e2 = Edge(1,2,4)
j.addEdge(e2)
e3 = Edge(1,3,3)
j.addEdge(e3)
e4 = Edge(3,4,4)
j.addEdge(e4)
e5 = Edge(2,0,5)
j.addEdge(e5)
e6 = Edge(0,4,4)
j.addEdge(e6)

w = KruskalMST(j)
for x in w.edges():
	print(x)
