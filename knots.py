class Link:
	def __init__(self, n):
		self.n = n
	def inf(self,ar):
		self.inf = ar
	def zero_smoothing(self):
class Vertex:
	def __init__(self, type):
		self.type = type
#right up;left up; left down ; right down
	def neighbours(self,list):
		self.neighbours = list




		
# n = int(input())
# knot = Link(n)
# knot.inf = []
# for k in range(n+1):
# 	ar = list(map(str,input().split()))
# 	knot.inf.append(ar) 
# print(knot.inf)
