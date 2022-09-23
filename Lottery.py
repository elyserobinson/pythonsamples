'''
A program to play a lottery. The program randomly generates a two-digit number, prompts the user to enter a two-digit number, and determines whether the user wins according to the following rules:

1. If the user’s input matches the lottery in the exact order, the award is $10,000.
2. If all the digits in the user’s input match all the digits in the lottery number, the award is
$3,000.
3. If one digit in the user’s input matches a digit in the lottery number, the award is $1,000.
'''

import random

# Generate a lottery number
lottery = random.randint(0, 99)

# Prompt the user to enter a guess
guess = eval(input("Enter your lottery pick (2 digits): "))

# Get digits from lottery
lotteryDigit1 = lottery // 10
lotteryDigit2 = lottery % 10

# Get digits from guess
guessDigit1 = guess // 10
guessDigit2 = guess % 10

print("The lottery number is", lottery)

# Check the guess
if guess == lottery:
  print("Exact match: you win $10,000")
elif (guessDigit2 == lotteryDigit1 and \
     guessDigit1 == lotteryDigit2):
     print("Match all digits: you win $3,000")
elif (guessDigit1 == lotteryDigit1
     or guessDigit1 == lotteryDigit2
     or guessDigit2 == lotteryDigit1
     or guessDigit2 == lotteryDigit2):
    print("Match one digit: you win $1,000")
else:
  print("Sorry, no match")
