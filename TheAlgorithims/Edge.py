class Edge:
	def __init__(self,v,w,weight):
		self._v = v
		self._w = w 
		self._weight = weight

	def __str__(self):
		return "Edge with verticies:{0},{1}, Weight:{2}".format(self._v, self._w, self._weight)

	def weight(self):
		return self._weight

	def either(self):
		return self._v

	def other(self,vert):
		if vert == self._v:
			return self._w
		elif vert == self._w:
			return self._v
		else:
			raise ValueError('Inconsistent Edge provided')

	def __cmp__(self,other):
		if not isinstance(other,Edge):
			raise ValueError('Comparing non-edge instance to edge exception')

		if (self._weight < other.weight):
			return -1
		elif (self._weight > other.weight):
			return 1
		else:
			return 0

	
