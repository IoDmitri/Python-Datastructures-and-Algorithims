import time

class MergeSort():
	def __init__(self):
		print("mergeSort is alive and well")

	def sort(self,a):
		self.mergeSort(a,0,len(a)-1)

	def mergeSort(self,a,lo,hi):
		#split a down the middle recursivly and sort it
		if (hi <= lo):
			return 

		mid = lo + (hi-lo)//2 
		self.mergeSort(a,lo,mid)
		self.mergeSort(a,mid+1,hi)
		self.merge(a,lo,mid,hi)

	def merge(self,a,lo,mid,hi):
		aux = a[:]
		i = lo
		j = mid+1 

		for x in range(lo,hi+1):
			if i > mid:
				a[x] = aux[j]
				j += 1
			elif j > hi:
				a[x]  = aux[i]
				i += 1
			elif aux[i] < aux[j]:
				a[x] = aux[i]
				i+= 1
			else:
				a[x] = aux[j]
				j +=1

class MergeBU(MergeSort):
	def sort(self,a):
		n = len(a)
		size = 1
		while (size < n):
			low = 0
			while (low < n - size):
				mid = low + size -1
				high = min(low + (size*2)-1, n-1)
				self.merge(a,low,mid,high)
				low += (size *2)
			size *= 2


start_time = time.time()
sort = MergeBU()
j = [5,3,1,2,8,9,15,3,18,27,29,13,11,72,84,92,33,55,7,100,147,92,98,52,78]
sort.sort(j)
end_time = time.time() - start_time
print(j)
print("execution took:", end_time)

k = [5,3,1,2,8,9,15,3,18,27,29,13,11,72,84,92,33,55,7,100,147,92,98,52,78]
top_time = time.time()
topSort = MergeSort()
topSort.sort(k)
final_time = time.time() - top_time
print(k)
print("execution took:", final_time)

