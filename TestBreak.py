# A program to demonstrate the effect of using break in a loop.

sum = 0
number = 0

while number < 20:
    number += 1
    sum += number
    if sum >= 100:
        break

print("The nubmer is", number)
print("The sum is", sum)
