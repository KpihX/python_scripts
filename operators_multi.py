from math import*
import sys

def bye():
	input("\nGlad to have served you! Press 'Enter' to quit.")
	sys.exit()

def get_real(label='x', type=float):
	"""
	Prompt the user for input and convert it to a specified type.

	Args:
		label (str): The label to display when prompting for input.
		type (type): The type to convert the input to.

	Returns:
		The user input converted to the specified type.
	"""
	while True:
		x = input("\n" + label + " = ")
		if x.strip() == '':
			bye()
		try:
			x = type(x)
		except ValueError:
			print(f"\n!You didn't enter a/an {type}!")
			continue
		break
	return x

def print_func(h:str, before:str = "")-> bool:
	"""It evaluates and prints an expression h, managing errors. It returns True if operations were held normally and False else. It puts a message 'before', before printing the result if no error occurred. It returns True if no error occurred and False else."""
	assert type(h) == str, f"h={h} must be a str"
	assert type(before) == str, f"before={before} must be a str"
	try:
		print(before+str(eval(h)))
		return True
	except ValueError:
		print(f"\nThe entered function is not defined for aan entered value.")
	except ZeroDivisionError:
		print(f"\nThe entered function is not defined for an entered value, due to a division by 0 which occured while evaluating it")
	except SyntaxError:
		print(f"\nThe entered function is syntaxically incorrect.")
	except NameError:
		print(f"\nThe entered function has unknown python math functions.")
	except ArithmeticError:
		print(f"\nThe evaluation of the given function reaches the arithmetic limits of Python")

f = print("Welcome! This program aims to evaluate some values of a given multi-variable function!")

while True:
	n = input("\nEnter the number of variables : ")
	if n.isdigit() == True and n != '0':
		n = int(n)
		break
	print("\nYou didn't enter a non-zero integer!")

Vars = ','.join([f'x{i}' for i in range(n)])
f = input(f"\nEnter a valid math function to eval for the real variables Vars (Ex: 'x0**2*e**(-x1)-log(x1-1)'; avoid using functions with letter Vars in theirs names) : \nf({Vars}) = ")

while True:
	g = f
	X = ""
	for i in range(n):
		x = str(get_real(f"x{i}"))
		g = g.replace(f'x{i}', x)
		X += str(x) + ","
	X = X[:-1]
	print_func(g, f"\nf({X}) = {g} = ")

	answer = input("\nAgain? (y/n) ")
	if answer.lower() != 'y':
		break
			
bye()