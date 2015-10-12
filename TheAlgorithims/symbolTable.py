class SymbolTable():
	def __init__(self):
		self.keys = []
		self.values = []
		self.n = 0

	def size(self):
		return self.n

	def isEmpty(self):
		return self.n == 0

	def get(self,key):
		if (self.isEmpty()):
			return None
		i = self.rank(key)
		if (i < self.n and self.keys[i] == key):
			return self.values[i]
		else:
			return None 

	def put(self,key,value):
		if (self.isEmpty()):
			self.keys.append(key)
			self.values.append(value)
			self.n +=1
			return

		i = self.rank(key)
		#update the value on the key 
		if (i < self.n and self.keys[i] == key):
			self.value[i] = value
			return

		if (i == self.n-1):
			#i is the last value in the list
			self.keys.append(key)
			self.values.append(value)
		else:
			self.keys.insert(i,key)
			self.values.insert(i,value)
			#i isn't the last value, so append at index
		self.n +=1


	def rank(self,key):
		lo = 0
		hi = self.n-1
		while(lo <= hi):
			mid = lo + (hi-lo)/2
			if (self.keys[mid] > key):
				hi = mid-1
			elif (self.keys[mid] < key):
				lo = mid+1
			else:
				return mid
		return lo

	def show(self):
		#print("len of keys:", len(self.keys))
		#print("len of values:", len(self.values))
		for x in range(0,self.n):
			print '{} = {}'.format(self.keys[x], self.values[x])

	def keys(self):
		#this is a pure function
		return self.keys.copy

	def size(self):
		return self.n

	def delete(self,key):
		i = self.rank(key)
		if (self.keys[i] == key):
			#the key is within the look up table
			del self.keys[i]
			del self.values[i]
			self.n -=1
			return key
		else:
			#cannot delete something not in the table
			reutrn -1
		



st = SymbolTable()
st.put('a',"Hello")
st.put('b',"World")
st.put('c',"Something else")
st.show()
st.delete('a')
st.show()





		