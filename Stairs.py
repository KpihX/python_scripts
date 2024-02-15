def stairs(n:int, m:int):
	"""It returns S(n) where S(n+m)=S(n+m-1)+...+S(n)"""
	try:
		n = int(n)
		m = int(m)
		assert n > 0 and m > 0 and n >= m
	except:
		print("Les données entrées ne sont pas toutes valides!")
		return False
	
	if m == 1:
		return 1
	
	S = [1]
	for i in range(n):
		S.append(sum(S))
		if len(S) == m+1:
			S.pop(0)
			
	return S[-1]
	
r = 'o'

while r.lower() == 'o':
	n = input("Entrez le nombre de marches de l'escalier : ")
	m = input("Entrez le nombre maximum de pas pouvant être éffectués : ")
	s = stairs(n,m)
	if s == False:
		continue
	print(f"Vous avez {s} façon(s) de monter un tel escalier")
	r = input ("Voulez modifier les données ('o' ou 'n') ? ")

q = input("Ravi de vous avoir servi!")
