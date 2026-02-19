'''
# 1). Python Program to add two integer values.

aa = 10
bb = 20
print("Addition integer value of aa+bb:", aa+bb)
cc = aa+bb
print("Addition integer value of cc:", cc)

x,y,z = 5,10,20
print("Addition integer value of x+y+z:", x+y+z)
print("-"*50)

# 2). Python Program to subtract two integer values.

a1 = 50
b1 = 20
print("Subtraction integer value of a1-b1:", a1-b1)
c1 = a1-b1
print("Subtraction integer value of c1:", c1)
print("-"*50)

# 3). Python program to multiply two numbers.

a2 = 4
b2 = 2
print("Multiply value of a2*b2:", a2*b2)
c2 = a2*b2
print("Multiply value of c2:", c2)
print("-"*50)

#4). Python program to repeat a given string 5 times.
"""Input :
str1 = “SQATools”
Output :
“SQAToolsSQAToolsSQAToolsSQAToolsSQATools” """

str1 = "SQATools"
print("Result:", str1*5)
print("-"*50)

# 5). Python program to get the Average of given numbers.
#Formula: sum of all the number/ total number

a3 = 40
b3 = 50
c3 = 30
print("Average of given numbers:", (a3+b3+c3)/3)
print("-"*50)

'''# 6). Python program to get the median of given numbers.
"""Note: all the numbers should be arranged in ascending order
Formula : (n+1)/2
n = Number of values
Input : [45, 60, 61, 66, 70, 77, 80]
Output:  66"""
'''
print("-"*50)

# 7). Python program to print the square and cube of a given number.
"""Input :
num1 = 9
Output :
Square = 81
Cube =   729
"""
G = 9
print("Square of a give number 9 is:", G**2)
print("Cube of a given number 9 is:", G**3)
print("-"*50)

#8). Python program to interchange values between variables.
"""Input :
a = 10
b = 20
Output :
a = 20
b = 10"""

a = 10
b = 20
a,b = b,a
print("interchange values a:", a)
print("interchange values b:", b)
print("-"*50)

"""#9). Python program to solve this Pythagorous theorem.
Theorem : (a2 + b2 = c2)

Solution"""

print("-"*50)

# 10). Python program to solve the given math formula.
# Formula : (a + b)2 = a^2 + b^2 + 2ab
j = 5
k = 6
result = (j**2)+(2*j*k)+(k**2)
print("(a + b)2:", result)
print("-"*50)

# 11). Python program to solve the given math formula.
# Formula : (a – b)2 = a^2 + b^2 – 2ab
l = 8
m = 6
result = (l**2)+(m**2)-(2*l*m)
print("(a – b)2:", result)
print("-"*50)

# 12). Python program to solve the given math formula.
# Formula : a2 – b2 = (a-b)(a+b)
p = 10
q = 8
result = (p-q)*(p+q)
print("a2 – b2:", result)
print("-"*50)

# 13). Python program to solve the given math formula.
# Formula : (a + b)3 = a3 + 3ab(a+b) + b3
r = 4
s = 5
result = (r**3)+(3*r*s*(r+s))+(s**3)
print("(a + b)3:", result)
print("-"*50)

# 14). Python program to solve the given math formula.
# Formula : (a – b)3 = a3 – 3a2b + 3ab2 – b3
t = 5
u = 6
result = (t**3)-(3*t**2*u)+(3*t*u**2)-(u*3)
print("(a - b)3:", result)
print("-"*50)

# 15). Python program to calculate the area of the square.
# Formula : area = a*a
area = int(input("Enter the side of square:" ))
print("Area of square:", area**2)
'''