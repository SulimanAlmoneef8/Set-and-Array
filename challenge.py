# Enter three numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

# Swap the numbers
temp = a
a = b
b = c
c = temp

# Show the result
print("After swapping:")
print("a =", a)
print("b =", b)
print("c =", c)