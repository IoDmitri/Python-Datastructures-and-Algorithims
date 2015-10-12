from Stack import Stack
from Queue import Queue

class DepthFirstOrder:
	def __init__(self,digraph):
		self._pre = Queue()
		self._post = Queue()
		self._reversePost = Stack()
		self._marked = [False] * (digraph.v +1)

		for v in range(digraph.v +1):
			if self._marked[v] is False:
				self._dfs(digraph,v)

	def _dfs(self,dg,v):
		self._pre.enqueue(v)
		self._marked[v] = True

		for w in dg.adj(v):
			if self._marked[w] is False:
				self._dfs(dg,w)

		self._post.enqueue(v)
		self._reversePost.push(v)

	def pre(self):
		return self._pre

	def post(self):
		return self._post

	def reversePost(self):
		return self._reversePost

