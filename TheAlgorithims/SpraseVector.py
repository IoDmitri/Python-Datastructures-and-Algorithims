from HashTable import LinearProbeHT

class SparseVector:

	def __init__(self):
		self.st = LinearProbeHT()

	def size(self):
		return self.st.size()

	def put(self,i,x):
		self.st.put(i,x)

	def get(self,i):
		if not self.st.contains(i):
			return 0.0
		else:
			return self.st.get(i)

	def dot(self,that):
		assert isinstance(that,list)
		sm = 0.0

		for x in self.st.keys():
			sm += that[x] * self.get(x)

		return sm

