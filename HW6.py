# A test program that prompts the user to enter an enteger and reports whether the integer is a palindrome.


# Return the reversal of an integer, e.g. reverse (456) returns 654

def reverse(number):
    result = 0
    while number != 0:
        digit = number % 10
        result = result * 10 + digit
        number //= 10
    return result

# Return true if number is a palindrome
def isPalindrome(number):
    if reverse(number) == number:
        return True
    else:
        return False

def main():
    number = eval(input("Enter a 3 digit number: "))
    print("The reverse number is", reverse(number))
    
    if isPalindrome(number):
        print(number, "is a palindrome.")
    else:
        print(number, "is not a palindrome.")

main()







'''
A program to play a variation of the game of craps. As follows:

Roll two dice. Each die has six faces representing values 1, 2, ..., and 6, respectively.
Check the sum of the two dice. If the sum is 2, 3, or 12 (called craps), you
lose; if the sum is 7 or 11 (called natural), you win; if the sum is another value
(i.e., 4, 5, 6, 8, 9, or 10), a point is established. Continue to roll the dice until either
a 7 or the same point value is rolled. If 7 is rolled, you lose. Otherwise, you win.
Your program acts as a single player.
'''


import random
import sys

# Get a dice
def getDice():
    i1 = random.randint(1, 6)
    i2 = random.randint(1, 6)

    print("You rolled", i1, "+", i2, "=", i1 + i2)
    return i1 + i2

def main():
    dice = getDice()
    if dice == 7 or dice == 11:
        print("Natural! You win")
        sys.exit()
    elif dice == 2 or dice == 3 or dice == 12:
        print("Craps! You lose")
        sys.exit()

    point = dice
    print("Point is", point)
    
    dice = getDice()
    while dice != 7 and dice != point:
        dice = getDice()
    
    if dice == 7:
        print("You lose")
    else:
        print("You win")

main()









