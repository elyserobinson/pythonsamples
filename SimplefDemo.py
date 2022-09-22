# A program that prompts the user to enter an integer and if the number is a multiple of 5 it will display HiFive, if the number is divisible by 2, the program displays HiEven.

number = eval(input("Enter an integer: "))

if number % 5 == 0:
    print("HiFive")

if number % 2 == 0:
    print("HiEven")
