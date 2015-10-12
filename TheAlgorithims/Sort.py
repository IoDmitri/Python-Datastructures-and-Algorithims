import time
import random

class Sort:
	def __init__(self):
		print("sort is alive and well")

	def less(self,v,w):
		return (v-w) < 0

	def exchange(self,array,a,b):
		tempElm = array[a]
		array[a] = array[b]
		array[b] = tempElm

	def show(self,array):
		print(array)

	def isSorted(self,array):
		for x in range(1,len(array)):
			if (self.less(array(x), array(x-1))):
				return false
			return true

class Selection(Sort):
	def sort(self,array):
		n = len(array)
		for x in range(0,n):
			minVal = x
			for y in range(x+1,n):
				if (self.less(array[y],array[minVal])):
					minVal = y
			self.exchange(array,x,minVal)

class Insertion(Sort):
	def sort(self,array):
		for x in range(1, len(array)):
			j = x
			while (j > 0 and self.less(array[j],array[j-1])):
				self.exchange(array,j,j-1)
				j = j-1

class Shell(Sort):
	def sort(self,array):
		n = len(array)
		h = 1
		while(h < n/3):
			h = 3*h +1
			print("h is equal to:", h)
		while (h >= 1):
			for x in range(h,n):
				j = x
				while (j >= h and self.less(array[j],array[j-h])):
					self.exchange(array,j,j-h)
					j = j-h
					self.show(array)
			h = h/3

class MergeSort(Sort):
	def merge(self,left,right):
		if not left:
			return right
		if not right:
			return left
		l = 0
		r = 0

		if left[0] < right[0] :
			return [left[0]] + self.merge(left[1:], right)
		return [right[0]] + self.merge(left, right[1:])

	def merge_sort(self,ls):
		if len(ls) <= 1:
			return ls
		mid = len(ls) // 2
		left = self.merge_sort(ls[:mid])
		right = self.merge_sort(ls[mid:])
		return (self.merge(left,right))

class QuickSort(Sort):

	def sort(self,a):
		self.innerSort(a,0,len(a)-1)

	def innerSort(self,a,lo,hi):
		if (hi <= lo):
			return 
		j = self.partition(a,lo,hi)
		self.innerSort(a,lo,j-1)
		self.innerSort(a,j+1,hi)
		
	def partition(self,a,lo,hi):
		pivot = a[hi]
		i = lo-1
		for x in range(lo,hi):
			if a[x] <= pivot:
				i = i +1
				self.exchange(a,i,x)
		i = i+1
		self.exchange(a,i,hi)
		return i

class MaxPQ(Sort):
	def __init__(self,a):
		self.pq = [0]
		self.pq += a[:]
		self.n = len(self.pq)

	def __init__(self):
		self.pq = [0]
		self.n = 0
	def isEmpty(self):
		return self.n == 0

	def size(self):
		return self.n

	def insert(self,key):
		self.n+=1
		self.pq.append(key)
		print(self.size())
		self.swim(len(self.pq)-1)

	def swim(self,key):
		while(key > 1 and self.less(self.pq[key/2], self.pq[key])):
			self.exchange(self.pq,key/2,key)
			key = key/2

	def sink(self,key):
		while (2*key <= self.n):
			j = 2*key
			if (j < self.n and self.less(self.pq[j],self.pq[j+1])):
				j += 1
			if not (self.less(self.pq[key],self.pq[j])):
				self.exchange(self.pq,k,j)
				k = j
				break

	def delMax(self):
		mx = self.pq[1]
		self.exchange(self.pq,1,self.n)
		self.n -= 1
		del self.pq[-1]
		return mx

	def show(self):
		print(self.pq)
class HeapSort(Sort):
	def __init__(self):
		print("HeapSort is initialized")

	def sort(self,a):
		n = len(a)
		k = n/2
		while(k >= 1 ):
			self.sink(a,k,n)
			k -= 1

		while(n > 1):
			self.exchange(a,1,n)
			n -= 1
			sink(a,1,n)

	#def sink(self,array,begin,end):




#j = [5,3,1,2,8,9,15,18,27,29,13,11,72,84,92,33,55,7,100,147,92,98,52,78]
#j=[5,3,2,4,1,6,8,7,9]
#print("start of sort")
#shell_time = time.time()
#srt = QuickSort()
#srt.sort(j)
#srt.show(j)
#print("Execution took:", time.time() - shell_time)
j = [3,4,5,6]
z = MaxPQ()
z.insert(7)
z.insert(8)
z.insert(2)
z.insert(100)
z.insert(150)
z.insert(12)
z.delMax()
z.show


