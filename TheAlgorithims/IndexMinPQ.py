from minHeap import MinHeap 

class IndexMinPQ:

	def __init__(self,mx):
		if mx < 0:
			raise ValueError('Minimum size of an IndexMinPQ must be greater than 0')
		self.mx = mx 
		self.n = 0
		self.pq = [None] * (mx+1)
		self.keys = [None] * (mx+1)
		self.qp = [-1] * (mx+1)

	def __str__(self):
		return "IndexMinPQ of max:{0}, size:{1}, keys:{2}, queue:{3}".format(self.mx,self.n,self.keys,self.pq)

	def __indexBoundsCheck(self,i):
		if i < 0 or i > self.mx:
			raise ValueError('index out of bounds')

	def __keyContainmentCheck(self,i):
		if self.contains(i):
			raise ValueError('provided index is already contained within the priority queue')

	def __missingKeyCheck(self,i):
		if not self.contains(i):
			raise ValueError('Provided key is not contained within the priority queue')

	def isEmpty(self):
		return self.n == 0

	def contains(self,i):
		self.__indexBoundsCheck(i) 
		return not self.qp[i] == -1 

	def size(self):
		return self.n

	def insert(self,i,key):
		self.__indexBoundsCheck(i)
		self.__keyContainmentCheck(i)

		self.n += 1
		self.qp[i] = self.n
		self.pq[self.n] = i
		self.keys[i] = key
		self._swim(self.n)

	def minIndex(self):
		if (self.n == 0):
			raise ValueError('Priority Queue is emtpy exception')
		return self.pq[1]

	def minKey(self):
		if (self.n == 0):
			raise ValueError('Priority Queue is empty exception')
		return self.keys[self.pq[1]]

	def delMin(self):
		if self.n == 0:
			raise ValueError('Priority Queue is empty exception')

		mn = self.pq[1]
		self._exchange(1,self.n)
		self.n -= 1
		self._sink(1)
		self.qp[mn] = -1
		del self.keys[self.pq[self.n+1]] 
		self.pq[self.n+1] = -1
		return mn 

	def keyOf(self,i):
		self.__indexBoundsCheck(i)
		self.__keyContainmentCheck(i)
		return self.keys[i]

	def changeKey(self,i,key):
		self.__indexBoundsCheck(i)
		self.__missingKeyCheck(i)

		self.keys[i] = key
		self._swim(self.qp[i])
		self._sink(self.qp[i])

	def change(self,i,key):
		self.changeKey(i,key)

	def decreaseKey(self,i,key):
		self.__indexBoundsCheck(i)
		self.__keyContainmentCheck(i)

		if (self.keys[i] < key):
			raise ValueError('Calling decreaseKey with given argument will not strictly decrease the key')
		self.keys[i] = key
		self._swim(self.qp[i])

	def increaseKey(self,i,key):
		self.__indexBoundsCheck(i)
		self.__keyContainmentCheck(i)

		if self.keys[i] > key:
			raise ValueError('Calling increaseKey with given argument will not strictly increase the key')

		self.keys[i] = key
		sink(self.qp[i])

	def delete(self,i):
		self.__indexBoundsCheck(i)
		self.__keyContainmentCheck(i)

		index = self.qp[i]
		self._exchange(index,self.n)
		self.n -=1 
		self._swim(index)
		self._sink(index)
		del self.keys[i]
		self.qp[i] = -1

	def _greater(self,i,j):
		return self.keys[self.pq[i]] > self.keys[self.pq[j]] 

	def _exchange(self,i,j):
		swap = self.pq[i]
		self.pq[i] = self.pq[j]
		self.pq[j] = swap
		self.qp[self.pq[i]] = i
		self.qp[self.pq[j]] = j 

	def _swim(self,k):
		while (k > 1 and self._greater(k/2,k)):
			self._exchange(k,k/2)
			k = k/2 

	def _sink(self,k):
		while (2*k <= self.n):
			j = 2*k

			if (j < self.n and self._greater(j,j+1)):
				j += 1

			if not self._greater(k,j):
				break
			self._exchange(k,j)
			k = j 



		




