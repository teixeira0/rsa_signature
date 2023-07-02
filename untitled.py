# Cifra AES
# Rodrigo Teixeira Soares	19/0019760

import sys
import binascii

def aes_cypher(message, key):
	print("Cyphering...")
	result  = []
	key_index = 0
	message = message.lower()
	for i in range(len(message)):
		if (message[i] == ' '):
			result.append(' ')
		else:
			result.append(number_to_letter((letter_to_number(message[i]) + letter_to_number(key[key_index])) % 26))
			key_index = key_index + 1
			if (key_index >= len(key)):
				key_index = 0
	print("Cypher complete!")
	return ''.join(result)

# This function decyphers a given message
def aes_decypher(message, key):
	print("Decyphering...")
	result  = []
	key_index = 0
	message = message.lower()
	for i in range(len(message)):
		if (ord(message[i]) < 97 or ord(message[i]) > 122):
			result.append(message[i])
		else:
			result.append(number_to_letter((letter_to_number(message[i]) - letter_to_number(key[key_index])) % 26))
			key_index = key_index + 1
			if (key_index >= len(key)):
				key_index = 0

	print("Decyphering complete!")
	return ''.join(result)


# rsa_signature.py 1/2/3/4/5 message.txt key.txt result.txt
if (len(sys.argv) != 6 and len(sys.argv) != 5):
	raise Exception("Invalid arguments!")

operation = sys.argv[1] 
message_file = sys.argv[2]
key_file = sys.argv[3]
result_file = sys.argv[4]
language = 'ptbr'
if (len(sys.argv) == 6):
	language = sys.argv[5]
message = ""
key = ""
result = ""
with open(message_file) as f:
	message = f.read()

if (operation == "c"):
	with open(key_file) as f:
		key = f.read()
	result = cypher(message, key)

	# Saving to file
	with open(result_file, "w") as f:
		f.write(result)	

elif (operation == "d"):
	with open(key_file) as f:
		key = f.read()
	result = decypher(message, key)

	# Saving to file
	with open(result_file, "w") as f:
		f.write(result)	
		
elif (operation == "b"):
	(result, key) = break_cypher(message, language)

	# Saving key to file
	with open(key_file, "w") as f:
		f.write(key)	
	
	# Saving to file
	with open(result_file, "w") as f:
		f.write(result)
else:
	raise Exception("Invalid operation!")
