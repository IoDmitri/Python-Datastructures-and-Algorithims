from LinkedList import LinkedList
import math

class SeperateChainingHT:
	def __init__(self,m=997):
		self.n = 0
		self.m = m
		self.st = []
		for x in range(0,m):
			ll = LinkedList()
			self.st.append(ll)

	def show(self):
		for x in range(0,self.m):
			self.st[x].show()

	def _hash(self,key):
		j = hash(key)
		z = abs(j)
		x = z % self.m
		return x

	def get(self,key):
		return self.st[self._hash(key)].get(key)

	def put(self,key,value):
		self.st[self._hash(key)].append(key,value)
		self.n += 1

	def delete(self,key):
		#find the bucket the key is in
		#then call remove on the linkedList 
		self.st[self._hash(key)].remove(key)

class LinearProbeHT:

	def __init__(self,m=16):
		self.n = 0;
		self.m = m
		self.keys = [None] * self.m
		self.values = [None] * self.m 

	def _hash(self,key):
		j = hash(key)
		z = abs(j)
		x = z % self.m
		return x

	def put(self,key,value):
		if (self.n > self.m/2):
			self.resize(2*self.m)

		i = self._hash(key)

		while (self.keys[i] is not None):
			if (self.keys[i] == key):
				self.values[i] = value
				return
			else:
				i = (i+1) % self.m 

		self.keys[i] = key
		self.values[i] = value
		self.n += 1

	def get(self,key):
		i = self._hash(key)

		while (self.keys[i] is not None):
			if (self.keys[i] == key):
				return	self.values[i]
			else:
				# (1+1) % self.m means that if i >= m, it will return 1 and be in bounds 
				i = (i+1) % self.m

		return None


	def resize(self,cap):
		print("Resizing!")
		t = LinearProbeHT(cap)
		
		for x in range(0,self.m):
			if (self.keys[x] is not None):
				t.put(self.keys[x], self.values[x])

		self.keys = t.keys
		self.values = t.values
		self.m = t.m

	def contains(self,key):
		#validate that a given key is within our symbolTable
		return (self.get(key) is not None)

	def delete(self,key):
		#this is a bit more of a complex case
		if not self.contains(key):
			return 
		#at this point we are garaunteed that the key is contained 
		#inside our hashtable 
		i = self._hash(key)

		while (self.keys[i] != key):

			i = (i+1)% self.m

		#delete the key-value pair 	
		self.keys[i] = None
		self.values[i] = None

		i = (i+1)%self.m

		while (self.keys[i] is not None):
			keyToRedo = self.keys[i]
			valueToRedo = self.values[i]

			self.keys[i] = None
			self.values[i] = None

			self.n -= 1

			self.put(keyToRedo,valueToRedo)

			i = (i+1)%self.m 

		self.n -= 1

		if (self.n > 0 and self.n == self.m/8):
			self.resize(self.m/2)


	def keys(self):
		return self.keys

	def size(self):
		return self.n 

	def show(self):
		for x in range(0,self.m):
			print("key:{0}, value:{1}").format(self.keys[x], self.values[x])

