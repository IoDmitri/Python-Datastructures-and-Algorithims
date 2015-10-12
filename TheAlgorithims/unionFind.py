import time

class UnionFind:
    def __init__(self,size):
        self._id = list(range(0,size))
        self._count = size

    def find(self,elm):
       while(elm != self._id[elm]):
           elm = self._id[elm]
           self._id[elm] = self._id[self._id[elm]]
       return elm


       
    def union(self,p,q):
    	#this is the Quick-Union implementation
        pRoot = self.find(p)
        qRoot = self.find(q)
        if (qRoot == pRoot):
            return

        self._id[pRoot] = qRoot
        self._count = self._count-1

    def connected(self,p,q):
        return self._id[p] == self._id[q]
    
    def count(self):
        return self._count


class UnionFindSlow:
    def __init__(self,size):
        self._id = list(range(0,size))
        self._count = size

    def find(self,elm):
        while(elm != self._id[elm]):
           elm = self._id[elm]
        return elm

    def union(self,p,q):
        pID = self.find(p)
        qID = self.find(q)

        if (pID == qID):
            return

        for x in range(0,len(self._id)):
            if self._id[x] == pID:
                self._id[x] = qID
            self._count = self._count-1

    def count(self):
        return self._count

    def connected(self,p,q):
        return self._id[p] == self._id[q]

class WeightedUnionFind(UnionFind):
	def __init__(self,size):
		self._id = list(range(0,size))
		self._count = size
		self._sz = [1] * size

	def union(self,p,q):
		i = self.find(p)
		j = self.find(q)
		if (i == j):
			return

		if (self._sz[i] < self._sz[j]):
			self._id[i] = j
			self._sz[i] += self._sz[j]
		else:
			self._id[j] = i
			self._sz[j] += self._sz[i]
		self._count = self._count-1

