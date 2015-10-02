"""This program was created on 12/04/2015
It takes an user inputted string
encrypts it with the Transposition Cipher
and emails it to the users choice of person

https://www.facebook.com/AiiYourBaseRBel0ngToUs
"""
# SECURITY NOTICE
# THE EMAIL SENDS THE KEY NUMBER
# GET RID OF "myKey" in msg under main()
# to fix this

import sys
import smtplib
import random
import time
import transpositionEncrypt

def main():
    message = str(input("enter message here "))
    Email(message)


def Email(msg, toaddrs):

    # gets email to send to
    # i've put it here so timer isn't disrupted
    # starts a timer
    startTime = time.time()

    # Encrypts message with random key
    # TODO use Affine cipher as more secure
    myKey = random.randint(1, 26)
    msg = transpositionEncrypt.encryptMessage(myKey, msg)

    # Email credentials & the message with KEY
    fromaddr = ''
    print("\nThis may take a few seconds")
    username = ''
    password = ''
    KeySTR = str(myKey)
    msg = ("The key is ") + KeySTR + ("\n\n") + msg

    # The actual mail send
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(username, password)
    server.sendmail(fromaddr, toaddrs, msg)
    server.quit()

    # stops timer and prints time
    totalTime = round(time.time() - startTime, 2)
    print(totalTime)

    # closes program see close()
    close()


def close():
    print("\nProgram is now exiting\n")
    sys.exit()


if __name__ == '__main__':
    main()
