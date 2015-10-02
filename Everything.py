#!/usr/bin/env python3
# Linux SHEBANG not needed

# Activate Devmode to see true error messages instead of TRY-EXCEPT
# Error messages
# can help debug a program, opens and runs logging module
# DEVMODE is a constant, do not change name
# NOTE When DEVMODE is enabled it MAY record information you don't want to share
# such as Email message contents
DEVMODE = False

# TODO comment out other Python code in this directory
# TODO note encryption
# TODO make REMINDME() work
# TODO emailme() doesnt work if theres no internet, try & except clauses
# TODO improve Map() using Python book "automating the boring stuff in Python" by AL STEWGART
# TODO GET PYPERCLIP TO WORK
# TODO get google integration
# TODO sort out Notemake()

"""
This program was designed to do
everything from opening my most used websites
to sending my self an email

This program was made by Brandon on 27/03/2015
and was finished on 25/05/2015
Sucessfully tested and implemented Mac OSX integration
on 02/05/2015, 1 day before my 18th.

Program is hosted in DROPBOX so can have cross-platform note takings

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

# Import statements are put into the matching fuctions
# as to speed up the program, importing obviously takes time if all of this is at the top
# it doesn't adbide by PEP-8 but this program was made for speed and funcuionallity

# import statements used and where
# import smtplib in EMAIL() and EMAIL1()
# import webbrowser in BROWSER()
# import Strip (see strip.py, custom module) in PALINDROME()
# import sys in CLOSE()
# import pyperclip in Reverse
# import datetime in NoteMake()
# import webbrowser in MAP() and GoogleSearch()


# imports logging module, starts a debugging logger
# allows for easier debugging
import logging

logging.basicConfig(filename='ProgramLog.txt', level=logging.DEBUG,
                    format=' %(asctime)s - %(levelname)s- %(message)s')

if DEVMODE == False:
    # disables logging module
    logging.disable(logging.CRITICAL)


def main():
    logging.debug('\n\nStart of program')

    print("\nWhat Do you want to Do? Type Help for Help")
    Do = input("Enter here: ").upper()  # takes user input, makes it uppercase
    logging.info("This is the Do variable")
    logging.debug(Do)

    if Do == "EMAIL":
        msg = str(input("Enter a message to send here: "))
        logging.debug("User chose Email, this is users message")
        logging.debug(msg)
        toaddrs = "Brandonskerritt51@gmail.com"
        logging.info("EMAIL the user is sending to")
        logging.debug(toaddrs)
        email1(msg, toaddrs)  # see function emailme(msg)
        close()  # closes program

    elif Do == "BROWSER":
        logging.debug("User selected Browser")
        browser()  # see browser function
        close()  # closes program

    elif Do == "NOTE":
        # GOTO notemake() function
        logging.debug("User selected NOTE")
        NoteMake()

    elif Do == "READ":
        logging.debug("User selected READ")
        # goto readnote() function
        ReadNote()

        input("\nAny key to exit: ")  # lets user read message
        close()  # closes program

    elif Do == "PALINDROME":
        detect = str(input("Enter word here: "))  # stors user input as string
        logging.debug("Palindrome input is ")
        logging.debug(detect)
        palindrome(detect)  # see palindrome(detect)
        close()  # closes program

    elif Do.startswith("C"):
        logging.debug("user went to close with DO variable ")
        logging.debug(Do)
        close()
    # if user enters any word that starts with C, close the program

    elif Do == "EMAIL1":
        logging.debug("user selected EMAIL")
        # emails someone else, called email1 for brevity
        msg = str(input("Enter message here: "))  # takes user input as string in msg
        logging.debug("user entered this message ")
        logging.debug(msg)
        toaddrs = str(input("enter email address here: "))
        logging.debug("user entered this send to address ")
        logging.debug(toaddrs)
        email1(msg, toaddrs)  # see email1(msg)
        close()  # closes program

    elif Do.startswith("H"):
        logging.debug("user went to help with command ")
        logging.debug(Do)
        assistance()  # function has to be called assistance and not help
    # user cannot enter "help" because python will display its own help
    # screen, if user writes any word beginning with H, go to function
    # assistance()

    elif Do == "REVERSE":
        reverse = str(input("Enter here: "))  # takes user string
        logging.debug("User went to reverse with")
        logging.debug(reverse)
        reverse_msg(reverse)

    elif Do == "MAP":
        # opens up google maps with inputted adress
        address = str(input("Enter address here: "))
        logging.debug("user went to MAP with address ")
        logging.debug(address)
        map(address)

    elif Do.startswith("G"):
        # searches google for inputted search term
        search = str(input("Enter search term here: "))
        logging.debug("user went to google search with term")
        logging.debug(search)
        googleSearch(search)

    else:  # if invalid command is run, loop back around
        # to MAIN()
        print("\n" * 100)  # clears screen by printing 100 new lines
        print("Sorry, \"", Do.capitalize(), "\" is not a valid command.")
        logging.debug("user entered invalid command ")
        logging.debug(Do)
        # shows user what command they used and says its not valid
        assistance()
    # goes to help screen, in help screen it loads main() so it loops back round
    # to the start  of the program for brevity

    close()


def NoteMake():
    import datetime

    # TODO implement note encryption and decryption
    choiceNewFile = str(input("Do you want to make a new file? (Y)es or (N)o ")).capitalize()
    logging.debug("make a new file, yes or no. user chose ")
    logging.debug(choiceNewFile)
    if choiceNewFile.startswith("N"):
        fileName = "Notes.txt"
    else:
        fileName = input("Enter new File name here: ").capitalize()
        fileName += ".txt"
        logging.debug("user chose new file, called ")
        logging.debug(fileName)

    try:  # try except causes
        # opens file in read to check contents of file
        FileRead = open((fileName), 'r')  # opens file in read only mode
        FileCheck = FileRead.read()  # puts file contents into variable
        FileRead.close()

    except IOError as e:
        # if cant open file to read, try to create it
        try:
            print("\nAttempting to create file...\n")
            FileCheckFile = open((fileName), 'w+')
            FileCheck = FileCheckFile.read()
            FileCheckFile.close()
            if DEVMODE == True:
                print("First Try Cause")
                print(e)

        except IOError as e:
            # if cant create, error.
            print("\nFile could not be created. Try running this program"
                  " as Admin.")
            logging.critical("File didn't exist, couldn't make new file.")
            if DEVMODE == True:
                print("Second try Cause")
                print(e)
                logging.debug("error generated by second try cause ", e)

    if FileCheck != "":  # if filecheck is not equal to empty or there is stuff in it
        print("Do you want to (A)ppend or (W)rite to the file?")
        FileDecide = str(input("Enter here: ")).upper()
        logging.debug("file has stuff in it, user chose to (a)ppend or (w)rite ")
        logging.debug(FileDecide)

        if FileDecide.startswith("A"):
            File = open((fileName), 'a')

        elif FileDecide.startswith("W"):
            File = open((fileName), 'w')
    else:

        File = open((fileName), 'w')

    DateTime = datetime.datetime.now()
    logging.debug("date and time is ")
    logging.debug(DateTime)
    File.write("\n")
    File.write(str(DateTime))
    File.write("\n")
    Message = input("input Text here: ")  # takes user input
    File.write(Message)  # writes this to the file
    File.close()  # closes the file

    close()


def ReadNote():
    import glob

    FileList = [""]
    # reads the Notes.txt File and prints to screen
    # TODO allow abillity to choose which file to open
    ChoiceRead = input("Do you want to open a different file to"
                       " \"Notes.txt\"? (Y)es or (N)o ").upper()
    logging.debug("User chose to open new file to read to notes.txt yes or no ")
    logging.debug(ChoiceRead)

    if ChoiceRead.startswith("N"):
        Filename = ("Notes.txt")

    elif ChoiceRead.startswith("Y"):

        print("here is a list of Files you can open\n")
        for file in glob.glob("*.txt"):
            print((file), "\n")
            FileList.append(file)

        Filename = str(input("Enter file name here: ")).upper()
        Filename += ".txt"
    else:
        main()

    try:
        File = open((Filename), "r")  # if File cannot be read

    except IOError as e:
        # TODO dntn create random files below
        print("File does not exist. Creating File...\n")  # display this

        File = open("Notes.txt", 'w')

        File.write("This File is empty. Please use the NOTE\n"
                   " function of this program to write to this File.")

        print("This File is empty. Please use the NOTE\n"
              "function of this program to write to this File.\n")

        if DEVMODE == True:
            print(e)

        File.close()
        main()

    message = File.read()  # stores everything in File to Variable read
    print("\n")
    print(message)  # prints varaible read
    File.close()  # closes the File
    input("\nany key to close ")  # lets you read the File before closing
    close()  # closes


def reverse_msg(reverse):
    try:
        import pyperclip  # imports custom module

    except ImportError as e:  # catches any errors

        logging.error(e)

        print("Pyperclip could not be found.")  # prints this

    reverseNew = reverse[::-1]  # reverses variable reverse
    pyperclip.copy(reverseNew)  # copys varaible to getboard
    close()  # goes to close() function to close program


def assistance():
    # help screen, shows you what commands do what and stuff
    logging.info("Assistance has been called.")
    print("\n\t\tWelcome to the Help screen!")
    print("\nHere are the valid commands")

    print("\nEMAIL - Email your Self"
          "\nEMAIL1 - Email someone else"
          "\nBROWSER - Opens most frequently used websites"
          "\nNOTE - Writes to a text file "
          "\nREAD - Reads text file"
          "\nCLOSE - Closes Program"
          "\nPALINDROME - Checks if string is a palindrome"
          "\nREVERSE - Reverses a string"
          "\nMAP - Opens up google maps with entered address"
          "\nG - Opens up Google and googles search term entered\n")
    logging.info("\n\n")
    main()  # loads main() after help screen is showed


def email1(msg, toaddrs):
    # Simple Mail Transfer Protocol Library
    # required to send simple eMail

    import smtplib

    fromaddr = ''
    print("\nThis may take a few seconds")
    # asks user for the to address
    # stores it in string variable "toaddrs"

    # Credentials (if needed)
    username = ''
    password = ''
    # The actual mail send
    server = smtplib.SMTP('smtp.gmail.com:587')  # starts a gmail server with port 587
    server.starttls()  # idk what this does
    server.login(username, password)  # logs into gmail server
    server.sendmail(fromaddr, toaddrs, msg)  # sends mail
    server.quit()  # turns off server
    print("Completed! now exiting")


# completed, now exiting


def close():
    # I like to put the sys.exit close
    # as a function, so i can call it instead of writing
    # it every time i want to close the program
    import sys
    # import sys so i can close the program with sys.exit()
    if DEVMODE == True:
        input("any key to exit. ")
    logging.debug("END OF PROGRAM")
    sys.exit()


def palindrome(detect):
    # Strip strips all puncuation or/and spaces
    # see Strip.py in Everything.py's directory
    try:
        import Strip

    except ImportError as e:

        print("\nCannot find module named Strip.py"
              " Strip.py can be found in Dropbox\n")

        if DEVMODE == True:
            print(e)

        main()
    # If there is an error importing Strip.py
    # display custom error message, go back to main()

    detect = Strip.stripWithSpace(detect).lower()
    # takes detect varaible, strips all puncuation with spaces and
    # makes it lower case, this makes it easier to work with
    if detect == detect[::-1]:  # reverses entire string
        print("\n")
        print(detect.capitalize(), " is a palindrome")
    # if its the same as it is backwards, print (detect) is a palindrome
    else:
        print("\n")
        print(detect.capitalize(), " is not a palindrome")
    # if its not the same backwards, print (detect) is not a palindrome
    input("any key to exit")  # input any key to exit


def browser():
    import webbrowser
    # Import webbrowser allows me to open new tabs on default browser

    webbrowser.open_new_tab("https://www.twitter.com")  # opens Twitter
    webbrowser.open_new_tab("https://www.facebook.com")  # Opens Facebook
    webbrowser.open_new_tab("https://www.tumblr.com")  # opens Tumblr
    webbrowser.open_new("https://inbox.google.com")  # opens Inbox by Google


def map(address):
    # TODO what does sys.argv do
    import webbrowser  # sys #pyperclip
    # if len(sys.argv) > 1:
    # Get address from command line.
    # address = ' '.join(sys.argv[1:])
    # else:
    # Get address from clipboard.
    # address = pyperclip.paste()
    webbrowser.open('https://www.google.com/maps/place/' + address)


def googleSearch(search):
    import webbrowser

    webbrowser.open("https://www.google.co.uk/search?q=" + search)


# required in all programs, if the name "main" is called, run main()
# i do this instead of main() at the bottom so this can
# still be imported as a module
if __name__ == '__main__':
    main()
