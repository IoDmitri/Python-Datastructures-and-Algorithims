class Heap:
	def __init__(self):
		self.a = [0]
		self.n = 0

	def less(self,i,j):
		return (self.a[i] < self.a[j])

	def exchange(self,i,j):
	 	temp = self.a[i]
	 	self.a[i] = self.a[j] 
	 	self.a[j] = temp

	def swim(self,k):
	 	while (k>1 and self.less(k/2,k)):
	 		self.exchange(k/2,k)
	 		k = k/2

	def sink(self,k,l= None):
		if l is None:
			l = self.n
			
	 	while (2*k <= l):
	 		j = 2*k
	 		if (j<self.n and self.less(j,j+1)):
	 			j+= 1
	 		if not (self.less(k,j)):
	 			break
	 		self.exchange(k,j)
	 		k = j;
	 			

	def isEmpty(self):
	 	return self.n == 0

	def size(self):
	 	return self.n

	def insert(self,k):
	 	self.a.append(k)
	 	self.n +=1
	 	self.swim(self.n)

	def delMax(self):
	 	mx = self.a[1]
	 	self.exchange(1,self.n)
	 	self.n -=1
	 	del self.a[-1]
	 	self.sink(1)
	 	return mx 

	def show(self):
	 	print(self.a)

class HeapSort():
	def __init__(self):
		print("heapsort")

	def sort(self,a):
		j = Heap()
		for x in range(0,len(a)):
			j.insert(a[x])

		n = j.size()
		while (n > 1):
			j.exchange(1,n)
			n -= 1
			j.sink(1,n)
			
			j.show()





