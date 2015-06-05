class Link:
	def __init__(self, n):
		self.n = n
	def inf(self,ar):
		self.inf = ar
	def loop(self,comp,vertex):
		loop_edges = []
		for i in range(len(comp[vertex-1])):
			if comp[vertex-1][i] == vertex:
				loop_edges.append(i)
		return(loop_edges)
	def zero_smoothing(self,comp,vertex):#компонента и вершина
		le =  self.loop(comp,vertex)
		if len(le) == 0:
			comp[comp[vertex-1][1]-1][3] = comp[vertex-1][2]
			comp[comp[vertex-1][2]-1][4] = comp[vertex-1][1]
			comp[comp[vertex-1][3]-1][1] = comp[vertex-1][4]
			comp[comp[vertex-1][4]-1][2] = comp[vertex-1][3]
		if len(le) == 2:
			if le == [1,4]:
				comp[comp[vertex-1][2]-1][4] = comp[vertex-1][3]
				comp[comp[vertex-1][3]-1][1] = comp[vertex-1][2]
			if le == [2,3]:
				comp[comp[vertex-1][1]-1][3] = comp[vertex-1][4]
				comp[comp[vertex-1][4]-1][2] = comp[vertex-1][1]
			if le == [1,2]:
				self.inf.append([])
				comp[comp[vertex-1][3]-1][1] = comp[vertex-1][4]
				comp[comp[vertex-1][4]-1][2] = comp[vertex-1][3]
			if le == [3,4]:
				self.inf.append([])
				comp[comp[vertex-1][1]-1][3] = comp[vertex-1][2]
				comp[comp[vertex-1][2]-1][4] = comp[vertex-1][1]
		if len(le) == 4:
			self.inf.append([])
		del(comp[vertex-1])
	def one_smoothing(self,comp,vertex):
		le =  self.loop(comp,vertex)
		if len(le) == 0:
			comp[comp[vertex-1][1]-1][3] = comp[vertex-1][4]
			comp[comp[vertex-1][2]-1][4] = comp[vertex-1][3]
			comp[comp[vertex-1][3]-1][1] = comp[vertex-1][2]
			comp[comp[vertex-1][4]-1][2] = comp[vertex-1][1]
		if len(le) == 2:
			if le == [1,4]:
				self.inf.append([])
				comp[comp[vertex-1][2]-1][4] = comp[vertex-1][3]
				comp[comp[vertex-1][3]-1][1] = comp[vertex-1][2]
			if le == [2,3]:
				self.inf.append([])
				comp[comp[vertex-1][1]-1][3] = comp[vertex-1][4]
				comp[comp[vertex-1][4]-1][2] = comp[vertex-1][1]
			if le == [1,2]:
				comp[comp[vertex-1][1]-1][3] = comp[vertex-1][4]
				comp[comp[vertex-1][2]-1][4] = comp[vertex-1][3]
			if le == [3,4]:
				comp[comp[vertex-1][3]-1][1] = comp[vertex-1][2]
				comp[comp[vertex-1][4]-1][2] = comp[vertex-1][1]
		if len(le) == 4:
			self.inf.append([])
		del(comp[vertex-1])

def is_int(str):
	try:
		int(str)
		return True
	except ValueError:
		return False

class Vertex:
	def __init__(self, n):
		self.num = n
#right up;left up; left down ; right down
	def neighbors(self,list):
		self.neighbors = list


n = int(input())# число несвязанных между собой компонент
knot = Link(n)
knot.inf = []
for j in range(n):#отдельно вводим данные для каждой компоненты
	m=int(input())#для каждой компоненты вводим число вершин в ней
	ar0 =[]
	for i in range(m):
		ar = list(map(str,input().split()))
		for j in range(len(ar)):
			if is_int(ar[j]) == True:#переводим номера вершин-соседей в integer
				ar[j] = int(ar[j])
		ar0.append(ar)
	knot.inf.append(ar0)

