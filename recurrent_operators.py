from math import*

def func_rec(f:str, x:float, F0:dict):
	"""It takes a function defined by induction, and its initial values in the form of a dictionary (keys are values and values are their images through f). It returns f(x) if no error and False else"""
	assert type(f) == str, f"f={f} must be a string"
	assert type(x) == float, f"x={x} must be a float"
	assert type(F0) == dict and all([type(key) == float and type(val) == float for key, val in F0.items()]), f"F0 must be a dict where all elts must be floats"
	if x in F0:
		return F0[x]
	if F0 != {}:
		m = min(F0) 
	else:
		m = inf
	g = '' #It will contain the final function to evaluate without induction parts
	try: #We will try to identify parts in the form of f(x-a) in f
		count = 0
		i = 0
		l = len(f)
		l0 = len(F0)
		while i < l:
			if f[i: i+4] != "f(x-":
				g += f[i]
				i += 1
				continue
			i += 4
			j = i
			bool = False
			# We verify if after '-', we have a positive float followed by ')''
			while i<l:
				if f[i].isdigit():
					i+=1
					continue 
				if f[i] == '.' and bool == False:
					i+=1
					bool = True
					continue 
				break				
			if i == l or f[i] != ')':
				assert False
			k = round(x-float(f[j: i]), 6)
			if k < m or isclose(k, x):
				assert False
			count +=1
			if count > l0:
				assert False
			y = func_rec(f, k, F0) #We evaluate the found recurring part in f before putting the result in g
			F0[k] = y
			g += str(y)
			i += 1
		return eval(g.replace('x', str(x))) # We then evaluate the final expression 
	except AssertionError or TypeError:
		print(f"\nf(x)={f} is not a valid expression of a recurrence function or needs more init values than those given.\n")
		raise

def isFloat(S:str):
	"""It evaluates whether S is an unsigned float or not"""
	try:
		x = float(S)
		return True
	except ValueError:
		return False

def print_func_rec(g:str, before:str = "")-> bool:
	"""It evaluates and prints an expression g defined by induction, managing errors. It returns True if operations were held normally and False else. It puts a message 'before', before printing the result if no error occurred. It returns True if no error occurred and False else."""
	assert type(g) == str, f"g={g} must be a str"
	assert type(before) == str, f"before={before} must be a str"
	try:
		print(before+str(eval(g)))
		return True
	except ValueError:
		print(f"\nThe entered function is not defined for an entered value")
	except ZeroDivisionError:
		print(f"\nThe entered function is not defined for an entered value, due to a division by 0 which occured while evaluating it")
	except SyntaxError:
		print(f"\nThe entered function is syntaxically incorrect.")
	except NameError:
		print(f"\nThe entered function has unknown python math functions.")
	except ArithmeticError:
		print(f"\nThe evaluation of the given function reaches the arithmetic limits of Python")
	except AssertionError or TypeError:
		pass

def prod_func_rec(func:str, start:float, end:str, step:float, F:dict)-> float:
	"""It returns the products of func(x) (defined by recurrence) for x going from 'start' to 'end' by step of 'step. The init values of func are in F"""
	return prod([func_rec(func, x, F) for x in range_float(start, end, step)])

def range_float(start:float, end:float, step:float = 1)-> list:
	"""It returns the floats between 'start' and 'end', starting at 'start', with a step of 'step'"""
	if step == 0:
		return [start]
	return [start+step*n for n in range(0, floor((end-start)/step)+1)]

def sum_func_rec(func:str, start:float, end:str, step:float, F:dict)-> float:
	"""It returns the sum of func(x) (defined by recurrence) for x going from 'start' to 'end' by step of 'step. The init values of func are in F'"""
	return fsum([func_rec(func, x, F) for x in range_float(start, end, step)])

f = input("Welcome! This program aims to evaluate some values of a given function defined by induction!\nEnter a valid math function (eventually defined by induction) to eval for a real variable x (Ex: 'e**x+f(x-1)+ln(f(x-2)'; avoid using functions with letter x like exp) : \nf(x) = ")

i=0
F = {}
bool = True
while True:
	print(f"\nYou are going to enter the init value {i} and its image through f. (An empty entry interrompts the process).")
	while True:
		x0 = input(f"\n\tx{i} = ")
		if x0.strip() == '':
			bool = False
			break
		if isFloat(x0):
			break
		print("You didn't enter a float")
	while bool:
		f0 = input(f"\n\tf(x{i}) = ")
		if f0.strip() == '':
			bool = False
			break
		if isFloat(f0):
			break
		print("You didn't enter a float")
	if not bool:
		break
	F[float(x0)] = float(f0)
	i +=1
			
while True:
	o = input("\nEnter the operation to do ('e' for evaluating f(x) for a given x ; 's' to sum f(x) in a given range and 'p' to evaluate the product of f(x) in a given range) (an empty entry interrupts the process) : ").lower()
	if o.strip() == '':
		break
	if o.lower() == 'e':
		while True:
			x = input("\nx = ")
			if x.strip() == '':
				break
			if not isFloat(x):
				print("\nYou didn't enter a float!")
				continue
			print_func_rec("func_rec(f, float(x), F)", f"\nf({x}) = ")
	if o in {'s', 'p'}:
		bool = True
		while bool:
			while True:
				start = input("\nstart = ")
				if start.strip() == '':
					bool = False
					break
				if isFloat(start):
					break
				print("You didn't enter a float")
			while bool:
				end = input("\nend = ")
				if end.strip() == '':
					bool = False
					break
				if isFloat(end):
					break
				print("You didn't enter a float")
			while bool:
				step = input("\nstep = ")
				if step.strip() == '':
					bool = False
					break
				if isFloat(step):
					break
				print("You didn't enter a float")
			if not bool:
				break
			start = float(start)
			end = float(end)
			step = float(step)
			if o == 's':
				print_func_rec ("sum_func_rec(f, start, end, step, F)", f"\nThe sum of f(x) for x going from {start} to {end} by step of {step} is : ")
			else:
				 print_func_rec ("prod_func_rec(f, start, end, step, F)", f"\nThe product of f(x) for x going from {start} to {end} by step of {step} is : ")
					
input("\nGlad to have served you! Press 'Enter' to quit.")