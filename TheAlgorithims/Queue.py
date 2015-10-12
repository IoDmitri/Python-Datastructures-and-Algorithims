from LinkedList import LinkedList

class Queue:

	def __init__(self):
		self._ls = LinkedList()
		self.size = 0 

	def __str__(self):
		return "Queue contains:{0}".format(self._ls)

	def __iter__(self):
		return self

	def next(self):
		if not self.isEmpty():
			j = self.dequeue()
			return j
		else:
			raise StopIteration()

	def enqueue(self,n):
		self._ls.append(n,None)
		self.size += 1

	def dequeue(self):
		j = self._ls.popHead()
		self.size -= 1
		return j.key

	def isEmpty(self):
		return self.size == 0 

	def show(self):
		self._ls.show()




