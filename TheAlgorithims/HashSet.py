from HashTable import LinearProbeHT 

class Set:
	def __init__(self,n=16):
		self.st = LinearProbeHT(n)

	def put(self,key):
		self.st.put(key,bool(True))

	def contains(self,key):
		return self.st.contains(key)

	def size(self):
		return self.st.size()

	def isEmpty(self):
		return self.size > 0

	def delete(self,key):
		self.st.delete(key)

	def show(self):
		self.st.show()


j = Set()

j.put(5)
j.put(7)
j.put(8)

print(j.contains(10))
print(j.contains(5))

j.show()