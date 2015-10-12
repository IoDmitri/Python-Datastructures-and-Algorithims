from MinPQ import MinPQ
from Queue import Queue 
from EdgeWeightedGraph import EdgeWeightedGraph
from Edge import Edge 

class LazyPrimMST:

	def __init__(self,ewg):
		#ewg is an edge weighted graph
		self.pq = MinPQ()
		self.marked = [False] * (ewg.v+1)
		self.mst = Queue()

		self._visit(ewg,0)

		while not self.pq.isEmpty():
			e = self.pq.dequeue()
			v = e.either()
			w = e.other(v)
			if (self.marked[v] == True and self.marked[w] == True):
				continue 
			self.mst.enqueue(e)
			if not self.marked[v] == True:
				self._visit(ewg,v)
			if not self.marked[w] == True :
				self._visit(ewg,w)



	def _visit(self,ewg,v):
		self.marked[v] = True
		for e in ewg.adj(v):
			if not self.marked[e.other(v)] == True :
				self.pq.enqueue(e)

	def edges(self):
		return self.mst

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

w = LazyPrimMST(j)
for x in w.edges():
	print(x)




