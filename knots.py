class Link:
	def __init__(self, n):
		self.n = n
	def inf(self,ar):
		self.inf = ar
	def loop(self,vertex):
		loop_edges = []
		for i in range(len(self.inf[vertex-1])):
			if self.inf[vertex-1][i] == vertex:
				loop_edges.append[i]
		return(loop_edges)
	def zero_smoothing(self,vertex):
		le =  self.loop(vertex)
		if len(le) == 0:
			self.inf[self.inf[vertex-1][1]-1][3]= self.inf[vertex-1][2]
			self.inf[self.inf[vertex-1][2]-1][4]= self.inf[vertex-1][1]
			self.inf[self.inf[vertex-1][3]-1][1]= self.inf[vertex-1][4]
			self.inf[self.inf[vertex-1][4]-1][2]= self.inf[vertex-1][3]
		# if len(le) == 2:
		# 	if le == [1,4]:
				
		if len(le) == 4:
			self.inf[vertex-1] = []

	def one_smoothing(self,vertex):
		self.inf[self.inf[vertex-1][1]-1][3]= self.inf[vertex-1][4]
		self.inf[self.inf[vertex-1][2]-1][4]= self.inf[vertex-1][3]
		self.inf[self.inf[vertex-1][3]-1][1]= self.inf[vertex-1][2]
		self.inf[self.inf[vertex-1][4]-1][2]= self.inf[vertex-1][1]
class Vertex:
	def __init__(self, n):
		self.num = n
#right up;left up; left down ; right down
	def neighbors(self,list):
		self.neighbors = list


num = ["1","2","3","4","5","6","7","8","9","0"]
n = int(input())
m = int(input())
knot = Link(n)
knot.inf = []
for i in range(m):
	ar = list(map(str,input().split()))
	for j in range(len(ar)):
		if ar[j] in num:
			ar[j] = int(ar[j])
	knot.inf.append(ar) 
print(knot.inf)
knot.zero_smoothing(1)
print(knot.inf)
