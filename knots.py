class Link:
	def __init__(self, n):
		self.n = n
	def inf(self,ar):
		self.inf = ar
	def zero_smoothing(self,vertex):
#find which vertex v1 is the 1st in v.neighbors(right up)
#find which vertex is the 3rd in v1.neighbors(left down)
#change 3rd v1.neighbors(left down) into 2nd in v.neighbours(left up)
		self.inf[self.inf[vertex-1][1]-1][3]= self.inf[vertex-1][2]
#find which vertex v2 is the 2nd in v.neighbors(left up)
#find which vertex is the 4th in v2.neighbors(right down)
#change 4th v2.neighbors(right down) into 1st in v.neighbours(right up)
		self.inf[self.inf[vertex-1][2]-1][4]= self.inf[vertex-1][1]
#find which vertex v3 is the 3rd in v.neighbors(left down)
#find which vertex is the 1st in v3.neighbors(right up)
#change 1st v3.neighbors(right up) into 4th in v.neighbours(right down)
		self.inf[self.inf[vertex-1][3]-1][1]= self.inf[vertex-1][4]
#find which vertex v4 is the 4th in v.neighbors(right down)
#find which vertex is the 2nd in v4.neighbors(left up)
#change 2nd v4.neighbors(left up) into 3rd in v.neighbours(left down)
		self.inf[self.inf[vertex-1][4]-1][2]= self.inf[vertex-1][3]
	def one_smoothing(self,vertex):
#find which vertex v1 is the 1st in v.neighbors(right up)
#find which vertex is the 3rd in v1.neighbors(left down)
#change 3rd v1.neighbors(left down) into 4th in v.neighbours(right down)
		self.inf[self.inf[vertex-1][1]-1][3]= self.inf[vertex-1][4]
#find which vertex v2 is the 2nd in v.neighbors(left up)
#find which vertex is the 4th in v2.neighbors(right down)
#change 4th v2.neighbors(right down) into 1st in v.neighbours(right up)
		self.inf[self.inf[vertex-1][2]-1][4]= self.inf[vertex-1][3]
#find which vertex v3 is the 3rd in v.neighbors(left down)
#find which vertex is the 1st in v3.neighbors(right up)
#change 1st v3.neighbors(right up) into 2nd in v.neighbours(left up)
		self.inf[self.inf[vertex-1][3]-1][1]= self.inf[vertex-1][2]
#find which vertex v4 is the 4th in v.neighbors(right down)
#find which vertex is the 2nd in v4.neighbors(left up)
#change 2nd v4.neighbors(left up) into 1st in v.neighbours(right up)
		self.inf[self.inf[vertex-1][4]-1][2]= self.inf[vertex-1][1]
class Vertex:
	def __init__(self, type):
		self.type = type
#right up;left up; left down ; right down
	def neighbors(self,list):
		self.neighbors = list
class Polynomial:
	def __init__(self,link):
		self.link = link

		
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
