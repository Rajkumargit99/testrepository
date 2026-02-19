'''
# 1). Python program to check given number is divided by 3 or not.
var1 = int(input("Enter the number: "))
if var1%3 == 0:
    print("given number is divided by 3:", var1)
else:
    print("given number is not divided by 3:", var1)
print("--------------------------------------------------------------")

# 2). If else program to get all the numbers divided by 3 from 1 to 30.
print("--------------------------------------------------------------")

# 3). If else program to assign grades as per total marks.
marks = int(input("Enter the marks: "))
if marks<40:
    print("Failed: ", marks)
elif marks>=40 and marks<=50:
    print("Grade C: ", marks)
elif marks>50 and marks<=60:
    print("Grade B: ", marks)
elif marks>60 and marks<=70:
    print("Grade A: ", marks)
elif marks>70 and marks<=80:
    print("Grade A+: ", marks)
elif marks>80 and marks<=90:
    print("Grade A++: ", marks)
elif marks>90 and marks<=100:
    print("Grade Excellent: ", marks)
else:
    print("Not a valid marks")
print("--------------------------------------------------------------")

# 4). Python program to check the given number divided by 3 and 5.
var2 = int(input("Enter the number: "))
if var2%3 == 0 and var2%5 == 0:
    print("the given number is divided with 3 and 5: ", var2)
else:
    print("the given number is not divided with 3 and 5: ", var2)
print("--------------------------------------------------------------")

# 5). Python program to print the square of the number if it is divided by 11.
var3 = int(input("Enter the value: "))
if var3%11 == 0:
    print("Entered value divided by 11 and the values is: ", var3**2)
else:
    print("Entered values not divided by 11: ", var3)
print("--------------------------------------------------------------")

# 6). Python program to check given number is a prime number or not.
print("--------------------------------------------------------------")

# 7). Python program to check given number is odd or even.
var4 = int(input("Enter the number: "))
if var4%2 == 0:
    print("The given number is even number: ", var4)
else:
    print("The given number is Odd number: ", var4)
print("--------------------------------------------------------------")

# 8). Python program to check a given number is part of the Fibonacci series from 1 to 10.
fib = [0,1,2,4,5,6,9,10,12,15,18,20,22,23,24,25,30]
num = int(input("Enter the number: "))
if num in fib:
    print("The iven number is available in series:", num)
else:
    print("The iven number is Not available in series:", num)
print("--------------------------------------------------------------")

# 9). Python program to check authentication with the given username and password.
user_name = input("Enter User name: ")
password = input("Enter password: ")
Result = user_name == password

if user_name == password:
    print("Valid user id and password")
else:
    print("Invalid user id and password")
print("--------------------------------------------------------------")

# 10). Python program to validate user_id in the list of user_ids.
id_list = [11,22,33,44,55,66,77,88,99,111]
id = int(input("Enter the id: "))
if id in id_list:
    print("Valid id: ", id)
else:
    print("Invalid id: ", id)
print("--------------------------------------------------------------")

# 11). Python program to print a square or cube if the given number is divided by 2 or 3 respectively.
var5 = int(input("Enter the number1: "))

if var5%2 == 0:
    print("Suare of the given value is: ", var5**2)
elif var5%3 == 0:
    print("Qube of the given value is: ", var5**3)
else:
    print("Not a valid number")
print("--------------------------------------------------------------")

# 12). Python program to describe the interview process.
round1 = input("Enter the status of 1st round: ")
round2 = input("Enter the status of 2nd round: ")

if round1 == "passed":
    print("Congratulation you have cleared 1st round")
    if round2 == "passed":
        print("Congratulation you have cleared 2nd round")
        print("You are placed")
    elif round2 == "failed":
        print("Oh 2nd round not cleared, Better luck next time")
    else:
        print("Not a valid answer")
elif round1 == "failed":
    print("Oh 1st round not cleared, Better luck next time")
else:
    print("Not a valid address")
print("--------------------------------------------------------------")
# 13). Python program to determine whether a given number is available in the list of numbers or not.
list_1 = [1,2,3,4,5,6,7,9,10]
list_2 = [11,22,33,44,55,66,77,88,99]
num_1 = int(input("Enter the number: "))
if num_1 in list_1:
    print(f"{num_1} The number is available in the list_1")
elif num_1 in list_2:
    print(f"{num_1} The number is available in the list_2")
else:
    print(f"{num_1} The number is Not available in any of the list")
print("--------------------------------------------------------------")

# 14). Python program to find the largest number among three numbers.
num_1 = int(input("Enter the 1st number: "))
num_2 = int(input("Enter the 2nd number: "))
num_3 = int(input("Enter the 3rd number: "))
if num_1 > num_2 and num_1 > num_3:
    print("1st number is the Greater")
elif num_2 > num_1 and num_2 > num_3:
    print("2nd number is the Greater")
elif num_3 > num_1 and num_3 > num_2:
    print("3rd number is the Greater")
else:
    print("No number is greater")
print("--------------------------------------------------------------")

# 15). Python program to check any person eligible to vote or not
age = int(input("Enter the age: "))
if 100 >= age >= 18:
    print("You are eligible for Vote")
elif 100 >= age < 18:
    print("You are Not eligible for Vote")
else:
    print("Invalid age")
print("--------------------------------------------------------------")

# 16). Python program to check whether any given number is a palindrome.
numb1 = input("Enter the palindrome number: ")
if numb1 == numb1[::-1]:
    print("Yes its a palindrome number:", numb1)
else:
    print("No its not a palindrome number:", numb1)
print("--------------------------------------------------------------")

# 17). Python program to check if any given string is palindrome or not.

# 18). Python program to check whether a student has passed the exam. If marks are greater than 35 students have passed the exam.
marks01 = int(input("Enter the marks: "))
if 100 >= marks01 >= 35:
    print("Student Passed")
elif 100 >= marks01 < 35:
    print("Student Failed")
else:
    print("Not valid number")
print("--------------------------------------------------------------")

# 19). Python program to check whether the given number is positive or not.

# 20). Python program to check whether the given number is negative or not.

# 21). Python program to check whether the given number is positive or negative and even or odd.
numb01 = int(input("Enter the number: "))
if numb01 > 0:
    #print("Its a positive number")
    if numb01 % 2 == 0:
        print("The given number is positive and even")
    else:
        print("The given number is positive and odd")
else:
    if numb01 % 2 == 0:
        print("The given number is Negative and even")
    else:
        print("The given number is Negative and odd")

# One line statement if_else_program.
var = int(input("Enter the number: "))
result = "even" if var%2 == 0 else "odd"
print("The give number is: ", result)

'''