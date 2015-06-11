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



		



		