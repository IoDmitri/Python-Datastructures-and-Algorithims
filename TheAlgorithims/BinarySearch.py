class BinarySearch():
	def __init__(self):
		print("binary search")

	def find(self,a,key):
		lo = 0
		hi = len(a)-1
		while (lo <= hi):
			mid = lo + (hi-lo)
			if (a[mid] < key):
				#mid is less then the key
				lo = mid+1
			elif (a[mid] > key):
				#mid is greater then the key
				hi = mid-1
			else:
				return mid
		#at this point we are unsucesful at 
		#finding the value we are looking for
		return -1
	def testFind(self,a,key):
		lo = 0
		hi = len(a)-1

		while(lo <= hi):
			mid = lo + (hi-lo)/2
			if (a[mid] > key):
				hi = mid-1
			elif (a[mid] < key):
				lo = mid+1
			else:
				return mid
		return lo

j = [1,3,5,8,9,10,12,15]

z = BinarySearch()

x = z.testFind(j,15)
print(x)
print("done")