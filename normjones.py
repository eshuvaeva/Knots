
#supporting functions
#for input
def is_int(str):
	try:
		int(str)
		return True
	except ValueError:
		return False
#for link smoothing
def check_loops(ar):
	if ar[1][1] == 2 and ar[2][1] == 1:
		return True
	if ar[1][1] == 4 and ar[2][1] == 3:
		return False
# for polynomial multiplication
def reduce(a):
	powers=[]
	norm = []
	for t in a:
		powers.append(t[1])
	powers = set(powers)
	ps =sorted(powers)
	for h in ps:
		k = 0
		for t in a:
			if t[1] == h:
				k = k + t[0]
		norm.append([k,h])
	return(norm)

# classes
class Link:
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
			# print(comp)
			# print(neighbor1)
			# print(comp[neighbor1-1])
			# print(n1_edge)
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
			if len(comp)>1:
				self.inf.append([])
		del(comp[vertex-1])	
		return self
	def one_smoothing(self,comp,vertex):
		le = self.loop(comp,vertex)
		if len(le) == 0:
			neighbor1 = comp[vertex-1][1][0]
			n1_edge = comp[vertex-1][1][1]
			neighbor4 = comp[vertex-1][4][0]
			n4_edge = comp[vertex-1][4][1]
			comp[neighbor1-1][n1_edge] = [neighbor4,n4_edge]
			comp[neighbor4-1][n4_edge] = [neighbor1,n1_edge]
			neighbor2 = comp[vertex-1][2][0]
			n2_edge = comp[vertex-1][2][1]
			neighbor3 = comp[vertex-1][3][0]
			n3_edge = comp[vertex-1][3][1]
			comp[neighbor2-1][n2_edge] = [neighbor3,n3_edge]
			comp[neighbor3-1][n3_edge] = [neighbor2,n2_edge]
		if len(le) == 2:
			if le == [1,4]:
				self.inf.append([])
				neighbor2 = comp[vertex-1][2][0]
				n2_edge = comp[vertex-1][2][1]
				neighbor3 = comp[vertex-1][3][0]
				n3_edge = comp[vertex-1][3][1]
				comp[neighbor2-1][n2_edge] = [neighbor3,n3_edge]
				comp[neighbor3-1][n3_edge] = [neighbor2,n2_edge]
			if le == [2,3]:
				self.inf.append([])
				neighbor1 = comp[vertex-1][1][0]
				n1_edge = comp[vertex-1][1][1]
				neighbor4 = comp[vertex-1][4][0]
				n4_edge = comp[vertex-1][4][1]
				comp[neighbor1-1][n1_edge] = [neighbor4,n4_edge]
				comp[neighbor4-1][n4_edge] = [neighbor1,n1_edge]
			if le == [1,2]:
				neighbor3 = comp[vertex-1][3][0]
				n3_edge = comp[vertex-1][3][1]
				neighbor4 = comp[vertex-1][4][0]
				n4_edge = comp[vertex-1][4][1]
				comp[neighbor3-1][n3_edge] = [neighbor4,n4_edge]
				
				comp[neighbor4-1][n4_edge] = [neighbor3,n3_edge]
			if le == [3,4]:
				neighbor1 = comp[vertex-1][1][0]
				n1_edge = comp[vertex-1][1][1]
				neighbor2 = comp[vertex-1][2][0]
				n2_edge = comp[vertex-1][2][1]
				comp[neighbor1-1][n1_edge] = [neighbor2,n2_edge]
				comp[neighbor2-1][n2_edge] = [neighbor1,n1_edge]
		if len(le) == 4:
			if check_loops(comp[vertex-1]) == False:
				self.inf.append([])
			if len(comp)>1:
				self.inf.append([])
		del(comp[vertex-1])
		return self
	def count_right(self):
		r =0
		for i in range(len(self.inf[0])):
			if  self.inf[0][i][0][1] == "r":
				r = r+1
		return r
	def count_left(self):
		l =0
		for i in range(len(self.inf[0])):
			if  self.inf[0][i][0][1] == "l":
				l = l+1
		return l

class LaurentPolynomial():
	def __init__(self,min_power,coeff):
		a = [min_power]
		for i in coeff:
			a.append(i)
		self.inf = a
	def __add__(self,other):
		new_coeff=[]
		coeff1=self.inf[1:]
		coeff2=other.inf[1:]
		if self.inf[0]>other.inf[0]:
			for i in range(self.inf[0]-other.inf[0]):
				z = [0]
				coeff1 = [0]+coeff1
		if self.inf[0]<other.inf[0]:
			for i in range(other.inf[0]-self.inf[0]):
				z = [0]
				coeff2 = [0]+coeff2
		if len(coeff1)>len(coeff2):
			for i in range(len(coeff1)-len(coeff2)):
				coeff2.append(0)
		if len(coeff2)>len(coeff1):
			for i in range(len(coeff2)-len(coeff1)):
				coeff1.append(0)
		for j in range(len(coeff1)):
			new_coeff.append(coeff1[j]+coeff2[j])
		min_power = min(self.inf[0],other.inf[0])
		new_p =LaurentPolynomial(min_power,new_coeff)
		return(new_p)
	
	def __mul__(self,other):
		new_coeff = []
		temp_coeff = []
		coeff1=self.inf[1:]
		coeff2=other.inf[1:]
		for i in range(len(coeff1)):
			for j in range(len(coeff2)):
				a = coeff1[i]*coeff2[j]
				shift1 = self.inf[0]
				shift2 = other.inf[0]
				power = i+shift1 + j+shift2
				temp_coeff.append([a,power])
		norm = reduce(temp_coeff)
		new_coeff = []
		for f in norm:
			new_coeff.append(f[0])
		min_power = norm[0][1]
		new_p = LaurentPolynomial(min_power,new_coeff)
		return(new_p)
	def __pow__(self,n):
		new_p = LaurentPolynomial(0,[1])
		for j in range(n):
			new_p = new_p * self
		return new_p
	def normal_division(self):
		coeff = self.inf[1:]
		for i in range(2,len(coeff),1):
			coeff[i] = coeff[i]-coeff[i-2]
		pol = LaurentPolynomial(self.inf[0]+1,coeff)
		print(pol.inf)
def all_unknots(link):
	c = 0
	for k in link.inf:
		if k != []:
			c = c+1
	if c>0:
		return False
	else:
		return True

def Kauffman(link):
	import copy
	if len(link.inf) == 0:
		print(LaurentPolynomial(0,[1]).inf)
		return LaurentPolynomial(0,[1])
	else:
		n = len(link.inf[0])
		if n == 0:
			p0 = LaurentPolynomial(-1,[1,0,1])
			p = p0**len(link.inf)
			#print(len(link.inf))
			return p
		else:
			kn0 = Link()
			kn0.inf=copy.deepcopy(link.inf)
			kn1 = Link()
			kn1.inf=copy.deepcopy(link.inf)
			v = len(kn0.inf[0])
			kn0.zero_smoothing(kn0.inf[0],v)
			kn1.one_smoothing(kn1.inf[0],v)
			q = LaurentPolynomial(1,[-1])
			if link.inf[0][v-1][0][0] == '-':
				pol = Kauffman(kn0)+q*Kauffman(kn1)
			if link.inf[0][v-1][0][0] == '+':
				pol = Kauffman(kn1)+q*Kauffman(kn0)
			return pol
def Jones(link):
	k = Kauffman(link)
	r = knot.count_right()
	l = knot.count_left()
	koe = LaurentPolynomial(0,[-1])**l
	pol1 = LaurentPolynomial(r-2*l,[1])
	jo = koe*pol1*Kauffman(link)
	return jo

n = int(input())# число несвязанных между собой компонент
knot = Link()
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
j = Jones(knot)
print(j.inf)
j.normal_division()
