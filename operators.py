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

def prod_func(func:str, start:float, end:str, step:float)-> float:
	"""It returns the products of func(x) for x going from 'start' to 'end' by step of 'step'"""
	return prod(eval(func.replace('x', str(x))) for x in range_float(start, end, step))

def range_float(start:float, end:float, step:float = 1)-> list:
	"""It returns the floats between 'start' and 'end', starting at 'start', with a step of 'step'"""
	if step == 0:
		return [start]
	return [start+step*n for n in range(0, floor((end-start)/step)+1)]

def sum_func(func:str, start:float, end:str, step:float)-> float:
	"""It returns the sum of func(x) for x going from 'start' to 'end' by step of 'step'"""
	return fsum(eval(func.replace('x', str(x))) for x in range_float(start, end, step))

f = input("Welcome! This program aims to evaluate some values of a given function!\nEnter a valid math function to eval for a real variable x (Ex: 'x**2*e**(-x)-log(x-1)'; avoid using functions with letter x like exp) : \nf(x) = ")

while True:
	o = input("\nEnter the operation to do ('e' for evaluating f(x) for a given x ; 's' to sum f(x) in a given range and 'p' to evaluate the product of f(x) in a given range) (an empty entry interrupts the process) : ").lower()
	if o.strip() == '':
		break
	if o.lower() == 'e':
		x = str(get_real("x"))
		g = f.replace('x', x)
		print_func(g, f"\nf({x}) = {g} = ")
	if o in {'s', 'p'}:
		start = get_real("start")
		end = get_real("end")
		step = get_real("step")

		if step == 0:
			bye()
		else:
			if o == 's':
				print_func("sum_func(f, start, end, step)", f"\nThe sum of f(x) for x going from {start} to {end} by step of {step} is : ")
			else:
				print_func("prod_func(f, start, end, step)", f"\nThe product of f(x) for x going from {start} to {end} by step of {step} is : ")
					
input("\nGlad to have served you! Press 'Enter' to quit.")