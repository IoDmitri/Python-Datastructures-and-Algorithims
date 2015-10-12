
class Node:
	def __init__(self,key,value):
		self.key = key
		self.value = value
		self.next = None

	def __str__(self):
		return "Key:{0}, Value:{1}".format(self.key,self.value)

class LinkedList:
	def __init__(self,key = None,value=None):
		self.head = None
		self.size = 0 
		if key is not None and value is not None:
			self.append(key,value)

	def __str__(self):
		z = self.head
		printList = []
		while (z is not None):
			printList.append(z)
			z = z.next
		return "Linked List contains:{0}".format(printList)

	def append(self,key,value):
		if self.head is None:
			self.head = Node(key,value)
		else:
			n = self.head 
			while (n.next is not None):
				n = n.next

			n.next = Node(key,value)
			self.size += 1


	def remove(self,key):
		if self.head is None:
			return

		if (self.head.key == key):
			self.head = self.head.next
		else:
			z = self.head

			while (z.next.key != key and z.next is not None):
				z = z.next


			if (z.key == key):
				if z.next is None:
					z.next = None 
			else:
				z.next = z.next.next

		self.size -= 1 

	def traverse(self,n):
		n = self.head
		while (n > 0):
			n = self.head.next

		return n 

	def get(self,key):
		if (self.head is None):
			return None
		else:
			j = self.head

			while (j.key != key and j.next is not None):
				j = j.next

			if (j.key == key):
				return j.value
			else:
				return None

	def popHead(self):
		if (self.head is None):
			return None
		z = self.head
		self.head = self.head.next
		return z 

	def addToFront(self,key,value):
		if (self.head is None):
			self.append(key,value)
		else:
			#get a reference to the head
			j = self.head
			#create the new node
			z = Node(key,value)
			#set z's next as the head
			z.next = j
			#set the head to z 
			self.head = z

	def show(self):
		z = self.head

		while (z is not None):
			print("Z is a node with key:{0}, value:{1}, next:{2}".format(z.key,z.value,z.next))
			z = z.next




