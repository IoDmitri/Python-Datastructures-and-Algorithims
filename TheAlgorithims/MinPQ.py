from minHeap import MinHeap
import collections
#priority queue that returns the lowest element 
class MinPQ:
	def __init__(self,items = None):
		self._minHeap = MinHeap()
		self.count = 0

		if isinstance(items,collections.Iterable):
			#if items have been supplied build a MinPQ from those items. 
			for elm in items:
				self.enqueue(elm)
			

	def __iter__(self):
		return self

	def next(self):
		if not self.isEmpty():
			return self.dequeue()
		else:
			raise StopIteration()

	def enqueue(self,n):
		self._minHeap.append(n)
		self.count += 1

	def dequeue(self):
		j = self._minHeap.delMin()
		self.count -= 1
		return j

	def isEmpty(self):
		return self.count == 0

	def show(self):
		print(self._minHeap)

