# transposition decrypt

import math
import pyperclip

def main():
    myMessage = "Aiiylsn aoghnn e  irMTsoau trm"
    myKey = 8
    
    plaintext = decryptMessage(myKey, myMessage)
    
    print(plaintext + '|')
    pyperclip.copy(plaintext)
    
def decryptMessage(key, message):
    numOfColumns = math.ceil(len(message) / key)
    numOfRows = key # this might be broken
    numOfShadedBoxes = (numOfColumns * numOfRows) - len(message)
    
    plaintext = [''] * numOfColumns
    
    col = 0
    row = 0
    
    for symbol in message:
        plaintext[col] += symbol
        col += 1
        
        if (col == numOfColumns) or (col == numOfColumns - 1 and row >= numOfRows - numOfShadedBoxes ):
            col = 0
            row += 1
    return ''.join(plaintext)

if __name__ == '__main__':
    main()
