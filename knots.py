def is_int(str):
	try:
		int(str)
		return True
	except ValueError:
		return False
def check_loops(ar):
	if ar[1][1] == 2 and ar[2][1] == 1:
		return True
	if ar[1][1] == 4 and ar[2][1] == 3:
		return False
class Link:
	def __init__(self, n):
		self.n = n
	def inf(self,ar):
		self.inf = ar
	def loop(self,comp,vertex):
		loop_edges = []
		for i in range(len(comp[vertex-1])):
			if comp[vertex-1][i][0] == vertex:
				loop_edges.append(i)
		return(loop_edges)
	def zero_smoothing(self,comp,vertex):
		le = self.loop(comp,vertex)
		if len(le) == 0:
			neighbor1 = comp[vertex-1][1][0]
			n1_edge = comp[vertex-1][1][1]
			neighbor2 = comp[vertex-1][2][0]
			n2_edge = comp[vertex-1][2][1]
			comp[neighbor1-1][n1_edge] = [neighbor2,n2_edge]
			comp[neighbor2-1][n2_edge] = [neighbor1,n1_edge]
			neighbor3 = comp[vertex-1][3][0]
			n3_edge = comp[vertex-1][3][1]
			neighbor4 = comp[vertex-1][4][0]
			n4_edge = comp[vertex-1][4][1]
			comp[neighbor3-1][n3_edge] = [neighbor4,n4_edge]
			comp[neighbor4-1][n4_edge] = [neighbor3,n3_edge]
		if len(le) == 2:
			if le == [1,4]:
				neighbor2 = comp[vertex-1][2][0]
				n2_edge = comp[vertex-1][2][1]
				neighbor3 = comp[vertex-1][3][0]
				n3_edge = comp[vertex-1][3][1]
				comp[neighbor2-1][n2_edge] = [neighbor3,n3_edge]
				comp[neighbor3-1][n3_edge] = [neighbor2,n2_edge]
			if le == [2,3]:
				neighbor1 = comp[vertex-1][1][0]
				n1_edge = comp[vertex-1][1][1]
				neighbor4 = comp[vertex-1][4][0]
				n4_edge = comp[vertex-1][4][1]
				comp[neighbor1-1][n1_edge] = [neighbor4,n4_edge]
				comp[neighbor4-1][n4_edge] = [neighbor1,n1_edge]
			if le == [1,2]:
				self.inf.append([])
				neighbor3 = comp[vertex-1][3][0]
				n3_edge = comp[vertex-1][3][1]
				neighbor4 = comp[vertex-1][4][0]
				n4_edge = comp[vertex-1][4][1]
				comp[neighbor3-1][n3_edge] = [neighbor4,n4_edge]
				comp[neighbor4-1][n4_edge] = [neighbor3,n3_edge]
			if le == [3,4]:
				self.inf.append([])
				neighbor1 = comp[vertex-1][1][0]
				n1_edge = comp[vertex-1][1][1]
				neighbor2 = comp[vertex-1][2][0]
				n2_edge = comp[vertex-1][2][1]
				comp[neighbor1-1][n1_edge] = [neighbor2,n2_edge]
				comp[neighbor2-1][n2_edge] = [neighbor1,n1_edge]
		if len(le) == 4:
			if check_loops(comp[vertex-1]) == True:
				self.inf.append([])
		del(comp[vertex-1])

n = int(input())# число несвязанных между собой компонент
knot = Link(n)
knot.inf = []
for j in range(n):#отдельно вводим данные для каждой компоненты
	m=int(input())#для каждой компоненты вводим число вершин в ней
	ar0 =[]
	for i in range(m):
		vertex_inf = []
		for j in range(5):
			edge = list(map(str,input().split()))
			for t in range(len(edge)):
				if is_int(edge[t]) == True:#переводим номера вершин-соседей в integer
					edge[t] = int(edge[t])
			vertex_inf.append(edge)
		ar0.append(vertex_inf)
	knot.inf.append(ar0)
knot.zero_smoothing(knot.inf[0],1)
print(knot.inf)
