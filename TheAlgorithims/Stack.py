#the linkedList API stores a key-value pair. This stack will only
#store a single value, as such we append(elm,None) to the list
from LinkedList import LinkedList

class Stack:
	def __init__(self):
		self.ls = LinkedList()
		self.size = 0

	def __str__(self):
		print("Stack size is:", self.size)
		if (self.isEmpty()):
			return "The stack is Empty"
		else:
			return "Stack contains:{0}".format(self.ls)

	def __iter__(self):
		return self

	def next(self):
		if not self.isEmpty():
			return self.pop()
		else:
			raise StopIteration()

	def push(self,elm):
		#the way the stack works is that the LinkedList is appended
		#form the front
		self.ls.addToFront(elm,None)
		self.size+= 1

	def pop(self):
		#The first element in the LL is the last element that's added
		#returning the head gives the last node placed onto the stack
		self.size -=1 
		return self.ls.popHead().key

	def isEmpty(self):
		return self.size == 0

	def show(self):
		print(self.ls)
