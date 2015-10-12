class MinHeap:
	def __init__(self):
		self._a = [0]
		self.count = 0;

	def __iter__(self):
		return self

	def __str__(self):
		return "MinHeap contains:{0}".format(self._a)

	def next(self):
		if not self.isEmpty():
			return self.delMin()
		else:
			raise StopIteration()


	def _swim(self,k):
		#swim from the bottom to the top
		while (k> 1 and self._a[k] <self._a[k/2]):
			self._exchange(k,k/2)
			k = k/2

	def _exchange(self,x,y):
		#store _a[x] in w 
		w = self._a[x]
		#set _a[x] equal to _a[y]
		self._a[x] = self._a[y]
		#set _a[y] to w 
		self._a[y] = w

	def _sink(self,k,l=None):
		if l is None:
			l = self.count

		while (2*k <= l):
			j = 2*k
			#if _a[j] is bigger then _a[j+1] choose the smaller element
			if not j+1 > l and self._a[j] > self._a[j+1]:
				j += 1 
			if (j < self.count and self._a[k] > self._a[j]):
				#k is before j, so if k is bigger, exchange the elements
				self._exchange(k,j)
			if not (self._a[k] > self._a[j]):
				#if k is bigger then j, we have swam deep enough 
				#to maintain the heap invarient
				break
			k = j


	def append(self,n):
		#add n as the last item of a
		self._a.append(n)
		self.count += 1
		self._swim(self.count)

	def delMin(self):
		mn = self._a[1]
		self._exchange(1,self.count)
		self.count -= 1
		#delete the last element
		del self._a[-1]
		self._sink(1)
		return mn

	def isEmpty(self):
		return self.count < 1




			