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

class Vertex:
	def __init__(self, n):
		self.num = n
#right up;left up; left down ; right down
	def neighbors(self,list):
		self.neighbors = list

def is_int(str):
	try:
		int(str)
		return True
	except ValueError:
		return False

n = int(input())# number of disconnected components
knot = Link(n)
knot.inf = []
for j in range(n):#separate input for each component
	m=int(input())#number of vertices in each component
	ar0 =[]
	for i in range(m):
		ar = list(map(str,input().split()))
		for j in range(len(ar)):
			if is_int(ar[j]) == True:#numbers of neighbor vertices converted to integer
				ar[j] = int(ar[j])
		ar0.append(ar)
	knot.inf.append(ar0) 

