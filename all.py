#supporting functions
#for input
def is_int(str):
	try:
		int(str)
		return True
	except ValueError:
		return False
#for link smoothing
def check_loops(ar):#checks which type of loop there is
	if ar[1][1] == 2 and ar[2][1] == 1:
		return True
	if ar[1][1] == 4 and ar[2][1] == 3:
		return False
# for polynomial multiplication
def reduce(a):# reduction of the additive components
	powers=[]
	norm = []
	for t in a:
		powers.append(t[1])
	powers = set(powers)#a set of all power numbers is created
	ps =sorted(powers)
	for h in ps:#all the items for each power are found
		k = 0
		for t in a:
			if t[1] == h:
				k = k + t[0]#all the items with the same power are put together
		norm.append([k,h])
	return(norm)

# classes
class Link:
	def inf(self,ar):
		self.inf = ar
	def loop(self,comp,vertex):#checkes if a vertex has any loops
		loop_edges = []
		for i in range(len(comp[vertex-1])):
			if comp[vertex-1][i][0] == vertex:
				loop_edges.append(i)
		return(loop_edges)
	def zero_smoothing(self,comp,vertex):
		le = self.loop(comp,vertex)
		if len(le) == 0:#if a vertex has no loops 
			neighbor1 = comp[vertex-1][1][0]
			n1_edge = comp[vertex-1][1][1]
			neighbor2 = comp[vertex-1][2][0]
			n2_edge = comp[vertex-1][2][1]
			#first and second edges merge and connect the neighbours
			comp[neighbor1-1][n1_edge] = [neighbor2,n2_edge]
			comp[neighbor2-1][n2_edge] = [neighbor1,n1_edge]
			neighbor3 = comp[vertex-1][3][0]
			n3_edge = comp[vertex-1][3][1]
			neighbor4 = comp[vertex-1][4][0]
			n4_edge = comp[vertex-1][4][1]
			#third and fourth edges merge and connect the neighbours
			comp[neighbor3-1][n3_edge] = [neighbor4,n4_edge]
			comp[neighbor4-1][n4_edge] = [neighbor3,n3_edge]
		if len(le) == 2:#if a vertex has one loop
			if le == [1,4]:
				neighbor2 = comp[vertex-1][2][0]
				n2_edge = comp[vertex-1][2][1]
				neighbor3 = comp[vertex-1][3][0]
				n3_edge = comp[vertex-1][3][1]
				#first and fourth edges are removed
				#second and third edges merge and connect the neighbours
				comp[neighbor2-1][n2_edge] = [neighbor3,n3_edge]
				comp[neighbor3-1][n3_edge] = [neighbor2,n2_edge]
			if le == [2,3]:
				neighbor1 = comp[vertex-1][1][0]
				n1_edge = comp[vertex-1][1][1]
				neighbor4 = comp[vertex-1][4][0]
				n4_edge = comp[vertex-1][4][1]
				#second and third edges are removed
				#first and fourth edges merge and connect the neighbours
				comp[neighbor1-1][n1_edge] = [neighbor4,n4_edge]
				comp[neighbor4-1][n4_edge] = [neighbor1,n1_edge]
			if le == [1,2]:
				self.inf.append([])#an unknot is added
				neighbor3 = comp[vertex-1][3][0]
				n3_edge = comp[vertex-1][3][1]
				neighbor4 = comp[vertex-1][4][0]
				n4_edge = comp[vertex-1][4][1]
				#second and first edges are removed
				#third and fourth edges merge and connect the neighbours
				comp[neighbor3-1][n3_edge] = [neighbor4,n4_edge]
				comp[neighbor4-1][n4_edge] = [neighbor3,n3_edge]
			if le == [3,4]:
				self.inf.append([])#an unknot is added
				neighbor1 = comp[vertex-1][1][0]
				n1_edge = comp[vertex-1][1][1]
				neighbor2 = comp[vertex-1][2][0]
				n2_edge = comp[vertex-1][2][1]
				#third and fourth edges are removed
				#second and first edges merge and connect the neighbours
				comp[neighbor1-1][n1_edge] = [neighbor2,n2_edge]
				comp[neighbor2-1][n2_edge] = [neighbor1,n1_edge]
		if len(le) == 4:# if a vertex has a double loop it either one or two unknots are added
			if check_loops(comp[vertex-1]) == True:
				self.inf.append([])
			if len(comp)>1:
				self.inf.append([])
		del(comp[vertex-1])	
		return self
	def one_smoothing(self,comp,vertex):
		le = self.loop(comp,vertex)
		if len(le) == 0:#if a vertex has no loops 
			neighbor1 = comp[vertex-1][1][0]
			n1_edge = comp[vertex-1][1][1]
			neighbor4 = comp[vertex-1][4][0]
			n4_edge = comp[vertex-1][4][1]
			#first and fourth edges merge and connect the neighbours
			comp[neighbor1-1][n1_edge] = [neighbor4,n4_edge]
			comp[neighbor4-1][n4_edge] = [neighbor1,n1_edge]
			neighbor2 = comp[vertex-1][2][0]
			n2_edge = comp[vertex-1][2][1]
			neighbor3 = comp[vertex-1][3][0]
			n3_edge = comp[vertex-1][3][1]
			#second and third edges merge and connect the neighbours
			comp[neighbor2-1][n2_edge] = [neighbor3,n3_edge]
			comp[neighbor3-1][n3_edge] = [neighbor2,n2_edge]
		if len(le) == 2:
			if le == [1,4]:
				self.inf.append([])#an unknot is added
				neighbor2 = comp[vertex-1][2][0]
				n2_edge = comp[vertex-1][2][1]
				neighbor3 = comp[vertex-1][3][0]
				n3_edge = comp[vertex-1][3][1]
				#first and fourth edges are removed
				#second and third edges merge and connect the neighbours
				comp[neighbor2-1][n2_edge] = [neighbor3,n3_edge]
				comp[neighbor3-1][n3_edge] = [neighbor2,n2_edge]
			if le == [2,3]:
				self.inf.append([])#an unknot is added
				neighbor1 = comp[vertex-1][1][0]
				n1_edge = comp[vertex-1][1][1]
				neighbor4 = comp[vertex-1][4][0]
				n4_edge = comp[vertex-1][4][1]
				#second and third edges are removed
				#first and fourth edges merge and connect the neighbours
				comp[neighbor1-1][n1_edge] = [neighbor4,n4_edge]
				comp[neighbor4-1][n4_edge] = [neighbor1,n1_edge]
			if le == [1,2]:
				neighbor3 = comp[vertex-1][3][0]
				n3_edge = comp[vertex-1][3][1]
				neighbor4 = comp[vertex-1][4][0]
				n4_edge = comp[vertex-1][4][1]
				#first and second edges are removed
				#third and fourth edges merge and connect the neighbours
				comp[neighbor3-1][n3_edge] = [neighbor4,n4_edge]
				comp[neighbor4-1][n4_edge] = [neighbor3,n3_edge]
			if le == [3,4]:
				neighbor1 = comp[vertex-1][1][0]
				n1_edge = comp[vertex-1][1][1]
				neighbor2 = comp[vertex-1][2][0]
				n2_edge = comp[vertex-1][2][1]
				#third and fourth edges are removed
				#first and second edges merge and connect the neighbours
				comp[neighbor1-1][n1_edge] = [neighbor2,n2_edge]
				comp[neighbor2-1][n2_edge] = [neighbor1,n1_edge]
		if len(le) == 4:# if a vertex has a double loop it either one or two unknots are added
			if check_loops(comp[vertex-1]) == False:
				self.inf.append([])
			if len(comp)>1:
				self.inf.append([])
		del(comp[vertex-1])
		return self
	def count_right(self):#number of right-handed vertices is counted
		r =0
		for i in range(len(self.inf[0])):
			if  self.inf[0][i][0][1] == "r":
				r = r+1
		return r
	def count_left(self):#number of left-handed vertices is counted
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
		#the lengths of coefficients array are equalized
		#zeroes added at the beginning of an array
		if self.inf[0]>other.inf[0]:
			for i in range(self.inf[0]-other.inf[0]):
				z = [0]
				coeff1 = [0]+coeff1
		if self.inf[0]<other.inf[0]:
			for i in range(other.inf[0]-self.inf[0]):
				z = [0]
				coeff2 = [0]+coeff2
		#zeroes added at the end of an array
		if len(coeff1)>len(coeff2):
			for i in range(len(coeff1)-len(coeff2)):
				coeff2.append(0)
		if len(coeff2)>len(coeff1):
			for i in range(len(coeff2)-len(coeff1)):
				coeff1.append(0)
		for j in range(len(coeff1)):#new coefficients and powers are counted
			new_coeff.append(coeff1[j]+coeff2[j])
		min_power = min(self.inf[0],other.inf[0])
		new_p =LaurentPolynomial(min_power,new_coeff)
		return(new_p)
	def __mul__(self,other):
		new_coeff = []
		temp_coeff = []
		coeff1=self.inf[1:]
		coeff2=other.inf[1:]
		# each element of the first polynomial is multiplied by each element of the second
		for i in range(len(coeff1)):
			for j in range(len(coeff2)):
				a = coeff1[i]*coeff2[j]
				shift1 = self.inf[0]
				shift2 = other.inf[0]
				power = i+shift1 + j+shift2#for each new element its power is counted
				temp_coeff.append([a,power])
		norm = reduce(temp_coeff)# reduction of the additive components
		new_coeff = []
		for f in norm:
			new_coeff.append(f[0])
		min_power = norm[0][1]
		new_p = LaurentPolynomial(min_power,new_coeff)
		return(new_p)
	def __pow__(self,n):#exponentiation for a non-negative integer
		new_p = LaurentPolynomial(0,[1])
		for j in range(n):
			new_p = new_p * self
		return new_p
	def printing(self):
		st_poly = ""
		po = self.inf[0]
		coeff = self.inf[1:]
		for i in range(len(coeff)):
			if i+po == 0:#prevents the printing of the variable
				if coeff[i]>0:
					if i == 0:
						st_poly = st_poly + " "+str(coeff[i])
					else:
						st_poly = st_poly + " + " + str(coeff[i])
				if coeff[i]<0:
					st_poly = st_poly +" - " + str((abs(coeff[i])))
			elif i+po == 1:#prevents the printing of a coefficient equal to 1
				if coeff[i] == 1:
					if i == 0:
						st_poly = st_poly + " q"
					else:
						st_poly = st_poly + " + q"
				if coeff[i] == -1:
					st_poly = st_poly + " - q"
				if coeff[i] > 0 and coeff[i] != 1:
					if i == 0:
						st_poly = st_poly + str(coeff[i]) + "q"
					else:
						st_poly = st_poly +" + "+ str(coeff[i]) + "q"
				if coeff[i] < 0 and coeff[i] != -1:
					st_poly = st_poly +" - " + str((abs(coeff[i]))) + "q"
			elif i+po < 0:#prints negative powers in brackets
				if coeff[i] == 1:
					if i == 0:
						st_poly = st_poly + " q^"+ "("+str(i+po)+")"
					else:
						st_poly = st_poly + " + q^"+"("+str(i+po)+")"
				if coeff[i] == -1:
					st_poly = st_poly + " - q^"+"("+str(i+po)+")"
				if coeff[i] > 0 and coeff[i] != 1:
					if i == 0:
						st_poly = st_poly + str(coeff[i]) + "q^"+"("+str(i+po)+")"
					else:
						st_poly = st_poly +" + "+ str(coeff[i]) + "q^"+"("+str(i+po)+")"
				if coeff[i] < 0 and coeff[i] != -1:
					st_poly = st_poly +" - " + str((abs(coeff[i]))) + "q^"+"("+str(i+po)+")"
			else:#polynomial printed in a common way
				if coeff[i] == 1:
					if i == 0:
						st_poly = st_poly + " q^"+ str(i+po)
					else:
						st_poly = st_poly + " + q^"+str(i+po)
				if coeff[i] == -1:
					st_poly = st_poly + " - q^"+str(i+po)
				if coeff[i] > 0 and coeff[i] != 1:
					if i == 0:
						st_poly = st_poly + str(coeff[i]) + "q^"+str(i+po)
					else:
						st_poly = st_poly +" + "+ str(coeff[i]) + "q^"+str(i+po)
				if coeff[i] < 0 and coeff[i] != -1:
					st_poly = st_poly +" - " + str((abs(coeff[i]))) + "q^"+str(i+po)
		print(st_poly)
	def normal_division(self):
		coeff = self.inf[1:]#division by (q+q^(-1))
		for i in range(2,len(coeff),1):
			coeff[i] = coeff[i]-coeff[i-2]
		pol = LaurentPolynomial(self.inf[0]+1,coeff)
		return(pol)

def Kauffman(link):
	import copy
	if len(link.inf) == 0:#empty set
		return LaurentPolynomial(0,[1])
	else:
		n = len(link.inf[0])
		if n == 0:#an unknot
			p0 = LaurentPolynomial(-1,[1,0,1])
			p = p0**len(link.inf)
			return p
		else:#the link will be copied
			kn0 = Link()
			kn0.inf=copy.deepcopy(link.inf)
			kn1 = Link()
			kn1.inf=copy.deepcopy(link.inf)
			v = len(kn0.inf[0])
			kn0.zero_smoothing(kn0.inf[0],v)
			kn1.one_smoothing(kn1.inf[0],v)
			q = LaurentPolynomial(1,[-1])
			#the recurrent formula
			if link.inf[0][v-1][0][0] == '-':
				pol = Kauffman(kn0)+q*Kauffman(kn1)
			if link.inf[0][v-1][0][0] == '+':
				pol = Kauffman(kn1)+q*Kauffman(kn0)
			return pol

def Jones(link):
	k = Kauffman(link)
	r = knot.count_right()
	l = knot.count_left()
	#the Jones polynomial is counted according to the formula
	koe = LaurentPolynomial(0,[-1])**l
	pol1 = LaurentPolynomial(r-2*l,[1])
	jo = koe*pol1*Kauffman(link)
	return jo
try:
	array = []
	f_read = open(input(), 'r')#a file is opened
	for line in f_read.readlines():
		line = line.strip()
		array.append(line)
	f_read.close()
	try:
		n = int(array[0])#number of vertices is defined
		m = int(array[1])#number of disconnected unknots is defined
		del(array[0])
		del(array[0])
		knot = Link()
		knot.inf = [[]]
		ar1 = []
		for el in array:
			el1 = list(el.split())
			ar1.append(el1)
		for j in range(n):#vertex characterization
			ar = ar1[:5]
			for e in ar:
				for t in range(len(e)):
					if is_int(e[t]) == True:
						e[t] = int(e[t])#converting into numbers from strings
			ar1 = ar1[5:]
			knot.inf[0].append(ar)
		if n == 0:
			for h in range(m-1):
				knot.inf.append([])
		else:
			for h in range(m):
				knot.inf.append([])
		print("Kauffman bracket:")
		if n == 0 and m == 0:
			print(" 1")
			print("That is an empty set.")
		else:
			Kauffman(knot).printing()
			j = Jones(knot)
			print("Jones polynomial:")
			j.normal_division().printing()
	except :
		print(" Could not calculate. An error occured. Change your data and try again.")
except IOError:
	print("No such file. Try again.")
