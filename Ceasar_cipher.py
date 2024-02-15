from string import ascii_uppercase as Upper, ascii_lowercase as Lower

print("Welcome this programs aims to cipher or decipher a message using the Caesar Cipher!\n\
	principle : For a given key 'key' (positive integer between 0 and 25), the letter N°i in the english alphabet is associated to the letter number j,\
where j is the rest of the Euclidean division of i+key by 26\n")

def Ceasar(msg:str, key:int)-> str:
	"""It returns the encrypted version of msg following the Cesar process"""
	return msg.translate(str.maketrans(Upper+Lower, Upper[key:]+Upper[:key]+Lower[key:]+Lower[:key]))

def inv_Ceasar(msg, key):
	"""It returns the decrypted version of msg following the Cesar process"""
	return msg.translate(str.maketrans(Upper[key:]+Upper[:key]+Lower[key:]+Lower[:key], Upper+Lower))

while True:
	key = input("Enter the key (integer in [0..25]; an empty entry interrupts the process) : ")
	print('')
	if key.strip() == '':
		break
	if key.isdigit() == False:
		print(f"'{key}' is not a positive integer!\n")
		continue
	key = int(key)
	if key > 25:
		print(f"'{key}' must be <= 25!\n")
		continue

	action = input("Enter the action to do ('c' for cipher and 'd' for decipher; an empty entry interrupts the process) : ").lower()
	print('')
	if action.strip() == '':
		break
	if action not in {'c', 'd'}:
		print(f"'{action}' is an invalid action!\n")
		continue
	
	msg = input("Enter the message to cypher (an empty entry interrupts the process) : ")
	print('')
	if msg.strip() == '':
		break

	if action == 'c':
		print("Encrypted message : ", Ceasar(msg, key), '\n')
	if action == 'd':
		print("Decrypted message : ", inv_Ceasar(msg, key), '\n')
	
	again = input("Again ? ('y' or 'n') (an entry different from 'y' interrompt the process) : " ).lower()
	print('')
	if again != 'y':
		break
		
input("Glad to have served you! Press 'Enter' to quit.")