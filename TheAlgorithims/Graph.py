#this API defines a graph class that represents a single graph with
#connected components among its verticies and edges. 
#this api assumes that verticies are labled with numbers 0-(positive inifnity)
class Graph:
	#takes in the amount of verticies that are expected
	def __init__(self,v=9):
		#number of verticies 
		self.v = v
		#number of edges
		self.e = 0
		#adj list
		#if there are more verticies then spaces, this list is resized
		self._adj = []
		for x in range(v+1):
			self._adj.append([])

	def v(self):
		#returns the number of veritices within the graph
		return self.v

	def e(self):
		#returns the number of edges within the graph
		return self.e 

	def addEdge(self,v,w):
		#add each element to each others adj list 
		self._adj[v].append(w)
		self._adj[w].append(v)
		self.e += 1

	def adj(self,v):
		#returns all verticies adjecent to a given vertex v 
		return self._adj[v]

	def test(self):
		j = Graph(5)
		j.addEdge(1,2)
		j.addEdge(1,3)
		j.addEdge(0,2)
		j.addEdge(5,1)
		j.addEdge(3,4)
		j.addEdge(0,4)
		print(j.adj(1))
		print(j.e)
		print(j.v)





