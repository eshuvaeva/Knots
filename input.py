def is_int(str):
	try:
		int(str)
		return True
	except ValueError:
		return False
class Link:
	def __init__(self, n):
		self.n = n
	def inf(self,ar):
		self.inf = ar


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
print(knot.inf)


