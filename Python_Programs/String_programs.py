
# 1). Write a Python program to get a string made of the first and the last 2 chars from a given string. If the string length is less than 2, return instead of the empty string
str_1 = "Welcome"
if len(str_1) <= 4:
    print("Yes its 2 letter word: ", str_1)
else:
    print(str_1[0:2:1]+str_1[-2:])
print("---------------------------------------------------------------------------")

# 2). Python string program that takes a list of strings and returns the length of the longest string.
list_1 = ["i", "am", "learning", "python", "programs", "for", "automation"]
temp1 = 0
for word1 in list_1:
    a1 = len(word1)
    if a1 > temp1:
        temp1 = a1
        print(temp1)
print("the final out put:",temp1)
print("---------------------------------------------------------------------------")
'''
# 3). Python string program to get a string made of 4 copies of the last two characters of a specified string (length must be at least 2).

print("---------------------------------------------------------------------------")
# 4). Python string program to reverse a string if it’s length is a multiple of 4.

print("---------------------------------------------------------------------------")
# 5). Python string program to count occurrences of a substring in a string.

print("---------------------------------------------------------------------------")
# 6). Python string program to test whether a passed letter is a vowel or consonant.

print("---------------------------------------------------------------------------")
# 7). Find the longest and smallest word in the input string.

print("---------------------------------------------------------------------------")
# 8). Print most simultaneously repeated characters in the input string.

print("---------------------------------------------------------------------------")
# 9). Write a Python program to calculate the length of a string with loop logic.

print("---------------------------------------------------------------------------")
# 10). Write a Python program to replace the second occurrence of any char with the special character $.
Input = “Programming”
Output = “Prog$am$in$”

print("---------------------------------------------------------------------------")
# 11). Write a python program to get to swap the last character of a given string.
Input = “SqaTool”
Output = “IqaTooS”

print("---------------------------------------------------------------------------")
# 12). Write a python program to exchange the first and last character of each word from the given string.
Input = “Its Online Learning”
Output = “stI enlino gearninL”

print("---------------------------------------------------------------------------")
# 13). Write a python to count vowels from each word in the given string show as dictionary output.
Input = “We are Learning Python Codding”
output = {“We” : 1, “are” : 2, “Learning” : 3, “Python”:1, “Codding”}

print("---------------------------------------------------------------------------")
# 14). Write a python to repeat vowels 3 times and consonants 2 times.
Input = “Sqa Tools Learning”
Ouput = “SSqqaaa TToooooollss LLeeeaaarrnniiinngg”

print("---------------------------------------------------------------------------")
# 15). Write a python program to re-arrange the string.
Input = “Cricket Plays Virat”
Output = “Virat Plays Cricket”

print("---------------------------------------------------------------------------")
# 16). Write a python program to get all the digits from the given string.
Input = “””
Sinak’s 1112 aim is to 1773 create a new generation of people who
understand 444 that an organization’s 5324 success or failure is
based on 555 leadership excellence and not managerial
acumen
“””
Output = [1112, 5324, 1773, 5324, 555]

print("---------------------------------------------------------------------------")
# 17). Write a python program to replace the words “Java” with “Python” in the given string.
Input = “JAVA is the Best Programming Language in the Market”
Output = “Python is the Best Programming Language in the Market”

print("---------------------------------------------------------------------------")
# 18). Write a Python program to get all the palindrome words from the string.
Input = “Python efe language aakaa hellolleh”
output = [“efe”, “aakaa”, “hellolleh”]

print("---------------------------------------------------------------------------")
# 19). Write a Python program to create a string with a given list of words.
Input = [“There”, “are”, “Many”, “Programming”, “Language”]
Output = There are many programming languages.

print("---------------------------------------------------------------------------")
# 20). Write a Python program to remove duplicate words from the string.
Input = “John jany sabi row john sabi”
output = “John jany sabi row”

print("---------------------------------------------------------------------------")
# 21). Write a Python to remove unwanted characters from the given string.
Input = “Prog^ra*m#ming”
Output = “Programming”

Input = “Py(th)#@&on Pro$*#gram”
Output = “PythonProgram”

print("---------------------------------------------------------------------------")
# 22). Write a Python program to find the longest capital letter word from the string.
Input = “Learning PYTHON programming is FUN”
Output = “PYTHON”

print("---------------------------------------------------------------------------")
# 23). Write a Python program to get common words from strings.
Input String1 = “Very Good Morning, How are You”
Input String1 = “You are a Good student, keep it up”
Output = “You Good are”

print("---------------------------------------------------------------------------")
# 24). Write a Python program to find the smallest and largest word in a given string.
Input = “Learning is a part of life and we strive”
Output = “a”, “Learning”

print("---------------------------------------------------------------------------")
# 25). Check whether the given string is a palindrome (similar) or not.
Input= sqatoolssqatools
Output= Given string is not a palindrome
'''