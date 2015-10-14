class DirectedEdge:
#source: The node from which the edge originates from
#destination: The node that the edge moves towards
#weight: Represents a value of the connection, does not necesarily refer to distance 
	def __init__(self,source,dest,weight):
		self.source = source
		self.dest = dest
		self.weight = weight

	def __str__(self):
		return "{0} -> {1}, with weight:{2}".format(self.source,self.dest,self.weight)