class Polynomial(object):
	def __init__(self, coeff):
		self.coeff = coeff
	def __add__(self,other):
		coeff=[]
		coeff1=self.coeff
		coeff2=other.coeff
		if len(coeff1)>len(coeff2):
			for i in range(len(coeff1)-len(coeff2)):
				coeff2.append(0)
		if len(coeff2)>len(coeff1):
			for i in range(len(coeff2)-len(coeff1)):
				coeff1.append(0)
		for j in range(len(coeff1)):
			coeff.append(coeff1[j]+coeff2[j])
		return(coeff)
	def __mul__(p1,p2):


		