"""
Write a Python program to print the four terms of the series,
which are equidistant, get the first and last number form the user.
eg- Input      1 and  7
     Output     1 3 5 7
"""
a = int(input("Enter 1st Number: "))
b = int(input("Enter 2nd Number: "))
c = b - a
c = c / 3
print(a, a + c, b - c, b)
