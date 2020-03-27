# K.<>. 
from passwordmeter import test # Strength and Feedback of password
from urllib.request import urlopen # English words library
from os.path import isfile
from random import choice,randint

# Download the file if not present
if not isfile('words.txt'):
    print ('Downloading words.txt ... ')
    url = "https://raw.githubusercontent.com/dwyl/english-words/master/words.txt"
    with open('words.txt', 'wb') as f:
        f.write(urlopen(url).read())

# \n as delimeter since a new word is on each line
words = open('words.txt', 'r').read().split("\n")

# words=open('myWords.txt', 'r').read().split("\n")

special_chars=['!','?','$','@','%'] # edit this to conform to password specifications

def create_password(num_words, num_numbers, num_special):
    pass_str=""
    #For loops append onto the string variable
    for _ in range(num_words): # Number of words in password
        pass_str += choice(words).lower().capitalize()
    for _ in range(num_numbers):  # Number of numbers in password
        pass_str += str(randint(0,9))
    for _ in range(num_special): # Number of special characters in password
        pass_str += choice(special_chars)
    return pass_str

def elite(string):
    for char in string:
        if char == 'a' or char == 'A':
            string = string.replace('a','4').replace('A','4')
        elif char == 'b' or char == 'B':
            string = string.replace('b','8').replace('B','8')
        elif char == 'c' or char == 'C':
            string = string.replace('c','(').replace('C','(')
        elif char == 'e' or char == 'E':
            string = string.replace('e','3').replace('E','3')
        elif char == 'l' or char == 'L':
            string = string.replace('l','1').replace('L','1')
        elif char == 'o' or char == 'O':
            string = string.replace('o','0').replace('O','0')
        elif char == 's' or char == 'S':
            string = string.replace('s','5').replace('S','5')
        elif char == 't' or char == 'T':
            string = string.replace('t','7').replace('T','7')
        else:
            pass
    return string

def main():
    num_words = int(input("Enter number of words >>> "))

    num_numbers = int(input("Enter number of numbers >>> "))

    num_special = int(input("Enter number of special characters >>> "))

    pass_str = create_password(num_words, num_numbers, num_special)

    # Testing strength of the password generated and giving feedback. Returned as tuple
    strength,feedback = test(pass_str) 

    print ("\nPassword: %s"%pass_str)
    print ("\nStrength: %0.3f"%strength)
    print ('The closer to 0 the strength value, the stronger the password is.\n')
    print ("\nFeedback: %s\n"%feedback)

    print("Feeling Adventurous (Y/N) ??? ")
    decision = input()

    if decision == 'y' or decision == 'Y':
        pass_str = elite(pass_str)
        print ("\nPassword (1337): %s"%pass_str)
    

if __name__ =="__main__":
    main()
