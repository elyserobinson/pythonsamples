# A program that prompts the user to enter three integers and displays them in increasing order.

order = eval(input("Enter three numbers separated by commas (1, 3, 5): "))
ordered = sorted(order)
print(ordered)

Enter three numbers separated by commas (1, 3, 5): 
6, 5000, 200
[6, 200, 5000]





# A program that prompts the user to enter a year, month, and day of the month, and then it displays the name of the day of the week.

year = eval(input("Enter year (2008): "))

m = eval(input("Enter month (1-12): "))
if m == 1:
    m = 13
    year -= 1
elif m == 2:
    m = 14
    year -= 1

j = year // 100

k = year % 100

q = eval(input("Enter the day of the month (1-31): "))

h = (q + (26 * (m + 1) // 10) + k + (k // 4) + (j // 4) + 5 * j) % 7

if h == 0:
    print("Day of the week is Saturday")
elif h == 1:
    print("Day of the week is Sunday")
elif h == 2:
    print("Day of the week is Monday")
elif h  == 3:
    print("Day of the week is Tuesday")
elif h == 4:
    print("Day of the week is Wednesday")
elif h == 5:
    print("Day of the week is Thursday")
elif h == 6:
    print("Day of the week is Friday")


Enter year (2008): 
1986
Enter month (1-12): 
11
Enter the day of the month (1-31): 
6
Day of the week is Thursday




# A program that simulates picking a card from a deck of 52 cards. Displays the rank and suit of the card.

import random

rank = random.randint(1, 13)
if rank == 13:
    rank = "ACE"
elif rank == 11:
    rank = "Jack"
elif rank == 12:
    rank = "Queen"
elif rank == 13:
    rank = "King"

suit = random.randint(0, 3)
if suit == 0:
    suit = "Clubs"
elif suit == 1:
    suit = "Diamonds"
elif suit == 2:
    suit = "Hearts"
elif suit == 3:
    suit = "Spades"

print("The card you picked is the", rank, "of", suit)


The card you picked is the 6 of Diamonds

