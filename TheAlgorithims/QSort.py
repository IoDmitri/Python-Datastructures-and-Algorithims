import random
import time

class QuickSort:
	def __init__(self):
		print("QuickSort is initialized")

	def swap(self,a,i,j):
		temp = a[i]
		a[i] = a[j]
		a[j] = temp

	def sort(self,a):
		self.innerSort(a,0,len(a))

	def innerSort(self,a,lo,hi):
		if (hi <= lo):
			return 
		j = self.partition(a,lo,hi)
		self.innerSort(a,lo,j)
		self.innerSort(a,j+1,hi)

	def partition(self,a,lo,hi):
		#get a random element of the array as our pivot
		p = random.randint(lo,hi-1)
		#assign pVal to the value of random
		pVal = a[p]
		#swap the last element with our pivot
		self.swap(a,p,hi-1)
		#i will be our wall
		i = lo-1

		for x in range(lo,hi):
			if a[x] < pVal:
				# move to the left
				i += 1
				self.swap(a,i,x)
			#now at end of the array
		i +=1 
		self.swap(a,i,hi-1)
		return i


#j = [5,3,4,1,2]
j = [5,3,1,2,8,9,15,18,27,29,13,11,72,84,92,33,55,7,100,147,92,98,52,78]
#j = list("easyquestion")
runtime = time.time()
qs = QuickSort()
qs.sort(j)
print(j)
print("total execution took:", time.time()-runtime)
