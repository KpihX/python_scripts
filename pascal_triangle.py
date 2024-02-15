print("Welcome! This program aims to print the pascal triangle with a given number of line.\n")

def Pascal(height:int):
	"It prints a pascal triangle of size height"
	assert type(height) == int and height >= 1, "the height of the Pascal triangle to print is not a strict positive integer"
	Pascal = [1]
	comb = lambda n,p: 0 if (p > n or p < 0) else 1 if p == 0 else n/p*comb(n-1,p-1)
	max = len(str(int(comb(height-1, round((height-1)/2)))))
	if max%2 == 1:
		max1 = round((max+1)/2)
		max2 = max
	else:
		max1 = round((max+2)/2)
		max2 = max+1
	for i in range(height):
		print(" "*(height-i-1)*max1, " ".join([str(elt).center(max2) for elt in Pascal]))
		Pascal = [1]+[Pascal[j]+Pascal[j+1] for j in range(len(Pascal)-1)]+[1]

empty = False
while True:
	n = input("Enter the number of lines (positive integer; an empty entry interrupts the process) : ")
	print('')
	if n.strip() == '':
		empty = True
		break
	if n.isdigit() == False or n == '0':
		print(f"'{n}' is not a strict positive integer!\n")
		continue
	break

if empty == False:
	Pascal(int(n))

input("\nGlad to have served you! Press 'Enter' to quit.")