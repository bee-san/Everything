# strip puncuation custom module
# 12 / 03 / 2015
# Brandon
# https://www.facebook.com/AiiYourBaseRBel0ngToUs


"""
This program was designed to strip puncuation
from a string

This program was made by Brandon in February 2015
and was finished in February 2015
If you have any suggestions or want to help
contact me at
https://www.facebook.com/AiiYourBaseRBel0ngToUs

This program abides by the rules of presentation for
PEP-8
shown here on
https://www.python.org/dev/peps/pep-0008/

You may use this code, or any features of this code
in your own work, as long as you link my page
and the BSD licensing, which can be copied directly
below.

https://www.facebook.com/AiiYourBaseRBel0ngToUs
*BSD licensed*

More info can be read here
http://opensource.org/licenses/BSD-3-Clause

"""

import sys
# Sys is required for Sys.exit() in close() function


def main():
    # runs through every function and strips everything

    message = str(input("enter message here to strip "))

    message1 = strip(message)
    message2 = stripWithSpace(message)
    message3 = stripSpaceOnly(message)

    print(message1)
    print(message2)
    print(message3)

    close()



def strip(message):
    # strips all basic puncuation

    # defines puncuations
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    # creates empty variable
    no_punct = ""
    # for every charecter in MESSAGE
    for char in message:
        # if charecter is not in puncuations
        if char not in punctuations:
            no_punct = no_punct + char
            # replaces puncuation with nothing
    return no_punct
    # returns non-puncuated string


def stripWithSpace(message):
    # strips all puncuation with Space

    # defines puncuations
    punctuations = ''' !()-[]{};:'"\,<>./?@#$%^&*_~'''
    # creates empty variable
    no_punct = ""
    for char in message:
        if char not in punctuations:
            no_punct = no_punct + char
            # replaces puncuation with nothing
    return no_punct


def stripSpaceOnly(message):
    # Strips Space only

    # defines puncuations
    punctuations = ''' '''
    # creates empty variable
    no_punct = ""
    for char in message:
        if char not in punctuations:
            no_punct = no_punct + char
            # replaces puncuation with nothing
    return no_punct


def stripLetters(message):
    # Strips only alphabetical letters

    # defines puncuations

    message = message.upper()
    # converts message to upper case, makes it easier to strip

    punctuations = '''ABCDEFGHIJKLMNOPQRSTUVWXYZ'''
    # creates empty variable
    no_punct = ""
    for char in message:
        if char not in punctuations:
            no_punct = no_punct + char
            # replaces puncuation with nothing
    return no_punct


def Reverse(message):
    # reverse a string

    # may be useful
    reverseTranslated = ''
    i = len(message) - 1
    while i >= 0:
        reverseTranslated = reverseTranslated + message[i]
        i = i - 1


def close():
    input("Any key to exit! ")
    sys.exit()

if __name__ == '__main__':
    main()