# Find the greatest common divisor of two integers.

n1 = eval(input("Enter first integer: "))
n2 = eval(input("Enter second integer: "))

d = 2
gcd = 1

while d <= n1 and d <= n2:
    if n1 % d == 0 and n2 % d == 0:
        for i in range(0, d-1):
            if n1 % (d - i) == 0 and n2 % (d - i) == 0:
                gcd = d
                break
            
    d += 1
    
print("The greatest common divisor for", n1, "and", n2, "is", gcd)
