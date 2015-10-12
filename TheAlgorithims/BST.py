class Node:
	def __init__(self,key,value,count,color = False):
		self.key = key
		self.value = value
		self.count = count
		self.left = None
		self.right = None
		self.color = color

	def __str__(self):
		return "Node with key: {0}, color:{1}. [Left is:{2}, right is:{3}]".format(self.key,self.color,self.left,self.right)


class BTree:
	def __init__(self):
		self.root = None

	def size(self):
		return self._size(self.root)
		
	def _size(self,node):
		if (node is None):
			return 0
		else: 
			return node.count		

	def get(self,key):
		return self._get(key,self.root)

	def _get(self,key,node):
		if (node is None):
			return None

		if (node.key < key):
			#the node's key is smaller than the provided key
			return self._get(key,node.right)

		elif (node.key > key):
			#node's key is bigger than the provided key
			return self._get(key,node.left)
		else :
			#node has been reached
			return node.value

	def put(self,key,value):
		if (self.root is None):
			self.root = Node(key,value,1)
			return self.root
		else:
			return self._put(key,value,self.root)

	def _put(self,key,value,node):
		if (node is None):
			node = Node(key,value,1)

		if (node.key < key):
			#kNode's key is bigger lets look right
			node.right = self._put(key,value,node.right,)
		elif(node.key > key):
			#Node's key is smaller lets look left 
			node.left = self._put(key,value,node.left)
		else:
			#update the node's value
			node.value = value
			node.size = self._size(node.left)+ self._size(node.right) +1 
		
		return node 



	def min(self):
		return _min(self.root).key

	def _min(self,node):
		if (node.left is None):
			return node
		else:
			return self._min(node.left)


	def floor(self,key):
		t = self._floor(key,self.root)
		if (t is None):
			return None
		return t.key

	def _floor(self,key,node):
		if (node is None):
			return None

		if (node.key == key):
			return node
		elif (node.key > key):
			return self._floor(key,node.left)

		t = self._floor(key,node.right)
		if (t is None):
			#the current node has no right member
			return node
		else:
			return t

	def select(self,k):
		return self._select(self,k,self.root).key

	def _select(self,k,node):
		if (node is None):
			return None

		t = self._size(node.left)

		if (t > k):
			return self._select(k,node.left)
		elif (t < k):
			return self._select(k-t-1,node.right)
		else:
			return x

	def rank(self,key):
		return self._rank(key,self.root)

	def _rank(self,key,node):
		if (node is None):
			return 0

		if (node.key > key):
			return self._rank(key,node.left)
		elif(node.key < key):
			return 1+ self._size(node.left) + self._rank(key,node.right)
		else:
			return self._size(node.left)

	def deleteMin(self):
		self.root = self._deleteMin(self.root)

	def _deleteMin(self,node):
		if (node.left is None):
			#the node has no left kids, so its the smallest
			return node.right 

		node.left = self._deleteMin(node.left)
		node.size = self._size(node.left) + self._size(node.right)+1
		return node

	def delete(self,key):
		if (self.root is None):
			return 
		else:
			self.root = self._delete(key,self.root)

	def _delete(self,key,node):
		if (node is None):
			return None

		if (node.key > key):
			node.left = self._delete(key,node.left)
		elif(node.key < key):
			 node.right = self._delete(key,node.right)
		else:
			#we found the node, lets go through our deletion cases
			if (node.left is None):
				# there is only a right child
				return node.right
			if (node.right is None):
				# there is only a left child
				return node.left
			t = node
			node = self._min(t.right)
			node.right = self._deleteMin(t.right)
			node.left = t.left

		node.size = self._size(node.left) + self._size(node.right) + 1
		return node 

	def show(self):
		self._show(self.root)

	def _show(self,node):
		if (node is None):
			return 
		self._show(node.left)
		print(node)
		self._show(node.right)

	def isEmpty(self):
		return (self.root is None)

class RBTree(BTree):
	global red 
	red = True
	global black
	black = False

	def isRed(self,node):
		if node is None:
			return False
		return node.color == red

	def _rotateLeft(self,node):
		print("rotating left")
		x = node.right
		node.right = x.left
		x.left = node
		x.color = node.color
		node.color = red
		x.count = node.count
		node.count = 1 + self._size(node.left) + self._size(node.right)
		return x 

	def _rotateRight(self,node):
		print("rotating right")
		x = node.left
		node.left = x.right
		x.right = node
		x.color = node.color
		node.color = red
		x.count = node.count 
		node.count = 1 + self._size(node.left) + self._size(node.right)
		return x

	def _flipColor(self,node):
		print("flipping colors")
		node.color = red
		if node.left is not None:
			node.left.color = black
		if node.right is not None:
			node.right.color = black 

	def put(self,key,value):
		#print("put being called, root is:{0}".format(self.root))
		self.root = self._put(key,value,self.root)
		#print "put/root", self.root
		self.root.color = black

	def _put(self,key,value,node):
		if node is None:
			return Node(key,value,1,red)

		if (key > node.key):
			#the key is larger than the nodes key, check the right
			node.right = self._put(key,value,node.right)
		elif (key < node.key):
			#key is smaller than the nodes current key, look left
			node.left = self._put(key,value,node.left)
		else:
			#node value == the given value
			node.value = value 

		if (self.isRed(node.right) and not self.isRed(node.left)):
			#the right node is red, the left is not
			#this is a violation of our invarient 
			node = self._rotateLeft(node)

		if ((node is not  None) and self.isRed(node.left) and self.isRed(node.left.left)):
			#the left node is right, but so is its left node
			#a violation of our invariant again 
			node = self._rotateRight(node)


		if ((node is not None) and self.isRed(node.right) and self.isRed(node.left)):
			#both nodes are red, again this is a violation
			self._flipColor(node)
      
		if node is not None:
			node.count = self._size(node.left) + self._size(node.right) + 1
		return node 


	def moveRedLeft(self,node):
		self._flipColor(node)
		if (self.isRed(node.right.left)):
			node.right = self._rotateRight(node.right)
			node = self._rotateLeft(node)

		return node

	def moveRedRight(self,node):
		self._flipColor(node)
		if not node.left.left is None and not self.isRed(node.left.left):
			node = self._rotateRight(node)
		return node 

	def balance(self,node):
		if self.isRed(node.right):
			node = self._rotateLeft(node)
		return node

	def delMin(self):
		#the key to this will be to make sure that we end up on the bottom
		#node
		#we can get there via _rotateRight and _rotateLeft until the node
		#that we want to delete is the bottom node.
		if  not self.isRed(self.root.right) and not self.isRed(self.root.left):
			self.root.color = red 
		self.root = self._delMin(self.root)

		if not self.isEmpty():
			self.root.color = black 


	def _delMin(self,node):
		if (node is None or node.left is None):	
			return None 

		if not self.isRed(node.left) and not self.isRed(node.left.left):
			node = self.moveRedLeft(node)

		node.left = self._delMin(node.left)
		return self.balance(node)

	def delete(self,key):
		if (self.root is None):
			return 

		if not self.isRed(self.root.left) and not self.isRed(self.root.right):
			self.root.color = red 

		self.root = self._delete(key, self.root)
		if not self.isEmpty():
			self.root.color = black 


	def _delete(self,key,node):
		if (key < node.key):
			if not self.isRed(node.left) and not self.isRed(node.left.left):
				node = self.moveRedLeft(node)
			node.left = self._delete(key,node.left)
		else:
			if self.isRed(node.left):
				node = self._rotateRight(node)

			if (node.key == key) and node.right is None:
				return None

			if not node.right is None and not self.isRed(node.right) and not self.isRed(node.right.left):
				node = self.moveRedRight(node)

			if (node.key == key):
				node.value = self.get((self._min(node.right)).key)
				node.key = (self._min(node.right)).key
				node.right = self._deleteMin(node.right)
			else:
				node.right = self._delete(key,node.right)

		return self.balance(node)





z = RBTree()
z.put('A', "hello")
z.put('B', 'World')
z.put('C', 'YOLO')
z.put('D', 'YACK')
z.put('E', 'DERP')
z.put('G', 'TEST')
z.put('I', 'Now What')
z.delete('G')
#z.put(5,"hello")
#z.put(7,"YOLO")
#z.put(4,"World")
#z.put(8,"Sup")
#z.delete(8)
z.show()
print("root is:", z.root.key)
print("root's left is:{0}, right is:{1}".format(z.root.left, z.root.right))











