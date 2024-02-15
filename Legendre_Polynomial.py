from fractions import Fraction as Fr
import math
import matplotlib.pyplot as plt
import numpy as np
from numpy.polynomial import Polynomial as Pol

def Legendre_polynomial(n:int)-> Pol:
	"""It returns in the form of a numpy polynomial, a Legendre polynomial : for n in lN, Ln(x) = 1/(2^n*n!)*Dn((x^2-1)^n)"""
	assert n >= 0
	Coefs = [0 for k in range(n+1)]
	for k in range(int(n/2)+1):
		Coefs[n-2*k] = Fr((-1)**k*math.comb(n, k)*math.perm(2*(n-k), n), (2**n*math.factorial(n)))
	return Pol(Coefs)

n = int(input("Welcome! This program aims to present you the Legendre polynomial of order <= n.\n\nEnter n : "))
x = np.linspace(-1, 1, 1000)
for k in range(1, n+1):
	L = Legendre_polynomial(k)
	print("\nL{}(x) = {:unicode}".format(k, L))
	plt.plot(x, L(x), label = f"L{k}(x)")
plt.title(f"Legendre polynomials of order <= {n}")
plt.legend()
plt.show()