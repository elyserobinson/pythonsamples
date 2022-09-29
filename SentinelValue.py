# Whenever a value is read, assign it to data and add it to sum if it is not zero.

data = eval(input("Enter an integer (the input ends " + "if it is 0): "))

# Keep reading data until the input is 0
sum = 0
while data != 0:
    sum += data
    
    data = eval(input("Enter an integer (the input ends " + "if it is 0): "))

print("The sum is", sum)
