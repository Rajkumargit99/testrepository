'''
# 1). Write a Python loops program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included).

for i in range(1500,2701):
    if i%7 ==0 and i%5 == 0:
        print(i,end=" ")
print("------------------------------------------------------------------------------------------")

# 2). Python Loops program to construct the following pattern, using a nested for loops.

# first loop iterate from 1 to 6
for i in range(1, 6):
    # inner loop iterate from 1 to value of i+1
    for j in range(1,i+1):
        # print * for each iteration of j
        print("*", end=" ")
    print()
# this is second section will iterate
# from 5 to 1 in decreasing order
for i in range(5, 1,-1):
    for j in range(1,i-1):
        print("*", end=" ")
    print()
print("------------------------------------------------------------------------------------------")

# 3). Python Loops program that will add the word from the user to the empty string using python.
word = input("Enter the word: ")
str_1 = ""
for i in range(len(word)):
    str_1 += word[i]   #str_1 = (str_1)+(word)
print(str_1)
print("------------------------------------------------------------------------------------------")

# 4). Python Loops program to count the number of even and odd numbers from a series of numbers using python.
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12,13,14)
even = 0
odd = 0
for b in numbers:
    if b%2 == 0:
        even += 1
    else:
        odd += 1
print("Number of even numbers: ", even)
print("Number of odd numbers: ", odd)
print("------------------------------------------------------------------------------------------")
'''

# 5). Write a program that prints all the numbers from 0 to 6 except 3 and 6 using python.

'''
6). Write a program to get the Fibonacci series between 0 to 20 using python.
Fibonacci Series : 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181

Solution
7). Write a program that iterates the integers from 1 to 30 using python. For multiples of three print “Fizz” instead of the number and for multiples of five print “Buzz”.
For numbers that are multiples of both three and five print “FizzBuzz”.

Solution
8). Write a program that accepts a word from the user and converts all uppercases in the word to lowercase using python.
Input : “SqaTOOlS”
Output : “sqatools”

Solution
9). Python loops program that accepts a string and calculates the number of digits and letters using python.
Input : “python1234”
Output :
Letters 6
Digits 4

Solution
10). Python for loop program to print the alphabet pattern ‘O’ using python.
Output:
  ***
*       *
*       *
*       *
*       *
*       *
   ***

Solution
Discover more
Python
python
11). Python Loops program to print all natural numbers from 1 to n using a while loop in python.

Solution
12). Write a program to print all natural numbers in reverse (from n to 1) using a while loop in python.

Solution
13). Python Loops program to print all alphabets from a to z using for loop
        Take chr method help to print characters with ASCII values
        chr(65) = ‘A’
        A-Z ASCII Range  65-90
        a-z ASCII Range  97-122
Solution
14). Python Loops program to print all even numbers between 1 to 100 in python.

Solution
15). Python Loops program to print all odd numbers between 1 to 100 using python.

Solution
16). Python Loops program to find the sum of all natural numbers between 1 to n using python.

Solution
17). Python program to find the sum of all even numbers between 1 to n using python.

Solution
18). Python Loops program to find the sum of all odd numbers between 1 to n using python.

Solution
Discover more
Python
NumPy
19). Write a program to count the number of digits in a number using python.

Solution
20). Write a program to find the first and last digits of a number using python.

Solution

# continue
for i in range(10): # i = 0
    if i == 3 or i == 5 or i == 7:
        continue # police man
    print(i)
print("---------------------------------------------------------------")

for i in range(20, 1, -1):
    if i == 12:
        break
    print(i)

# 41).  Python loops program to print the pattern T using Python Loops.
for i in range(3):
    for j in range(9):
        print("*", end=" ")
    print()
for i in range(6):
    for j in range(9):
        if j>5 and j<9:
            print("*", end=" ")
        else:
            print("", end=" ")
    print()


for row in range(0, 7):
        for column in range(0, 7):
            # here in first and last row we want to three *
            if (row == 0 or row == 6) and (1 < column < 5) :
                print("*", end=' ')
            # here from 2 to 6 row, * will print on 1 and 5 index only.
            elif (0 < row <= 5) and (column ==1 or column ==5):
                print("*", end=' ')
            else:
                print(" ", end=' ')
        print()
        
Print(--------------------------------------------------------------------------------)
#Testing:
for var in range(1,20):
    print(var)

var1 = ["raj", "Ravi", "kig"]
print(var1)

for v in var1:
    print(v)
'''