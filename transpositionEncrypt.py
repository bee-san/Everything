# transposition cipher encryption

import pyperclip

def main():
	myMessage = 'I really like cats' # Puts message here
	myKey = 8 # key number to be used
	

	ciphertext = encryptMessage(myKey, myMessage) # runs this functuon
	print(ciphertext + '|')
	# prints ciphertext with pipe charecter
	
	pyperclip.copy(ciphertext)
	#copies ciphertext to clipboard
	
def encryptMessage(key, message):

	ciphertext = [''] * key
	
	for col in range(key):
	
		pointer = col
		
		while pointer < len(message):
		
			ciphertext[col] += message[pointer]
			
			pointer += key
			#moves pointer
	return ''.join(ciphertext)

if __name__ == '__main__':
	main()
