# Python List Programs
list_1 = ["hari", "ravi", "raju", "kumar", "nag","raju", "kumar"]
print(list_1)
print(set(list_1))
var = set(list_1)
print(list(var))

print("---------------------------------------------------------------------------------")

list_2 = ["hari", "ravi", "raju", "kumar", "siva", "arun", "siva", "nag","raju", "kumar"]
ans = []
for name in list_2:
    if name not in ans:
        ans.append(name)
        #print(ans)
    else:
        continue
print(ans)
print("---------------------------------------------------------------------------------")

# 1). Python program to calculate the square of each number from the given list.
list_3 = [5,2,5,9,12,14,1,6,8,10,22]
result_1 = 0
for van_1 in list_3:
    result_1 = van_1 ** 2
    print("The value: ", van_1, "the suare value : ", result_1)

print("---------------------------------------------------------------------------------")

# 2). Python program to combine two lists.
list_4 = [1,2,3,4,5,6,7,9,10]
list_5 = [11,22,33,44,55,66,77,88,99]
print(list_4+list_5)

list_4.extend(list_5)
print(list_4)
print("---------------------------------------------------------------------------------")

# 3). Python program to calculate the sum of all elements from a list.
list_6 = [2,4,6,8,9,5,6,8]
result_2 = 0
for van_2 in list_6:
    print(van_2)
    if van_2 + result_2:
        result_2 = van_2
        print(result_2, end=" ")

'''
print("---------------------------------------------------------------------------------")
4). Python program to find a product of all elements from a given list.

print("---------------------------------------------------------------------------------")
5). Python program to find the minimum and maximum elements from the list.

print("---------------------------------------------------------------------------------")
6). Python program to differentiate even and odd elements from the given list.

print("---------------------------------------------------------------------------------")
7). Python program to remove all duplicate elements from the list.

print("---------------------------------------------------------------------------------")
8). Python program to print a combination of 2 elements from the list whose sum is 10.

print("---------------------------------------------------------------------------------")
9). Python program to print squares of all even numbers in a list.

print("---------------------------------------------------------------------------------")
10). Python program to split the list into two-part, the left side all odd values and the right side all even values.
Input = [5, 7, 2, 8, 11, 12, 17, 19, 22]
Output = [5, 7, 11, 17, 19, 2, 8, 12, 22]


print("---------------------------------------------------------------------------------")

11).  Python program to get common elements from two lists.
Input =
list1 = [4, 5, 7, 9, 2, 1]
list2 = [2, 5, 8, 3, 4, 7]
Outputt : [4, 5, 7, 2]

print("---------------------------------------------------------------------------------")
12). Python program to reverse a list with for loop.

print("---------------------------------------------------------------------------------")
13). Python program to reverse a list with a while loop.


print("---------------------------------------------------------------------------------")
14). Python program to reverse a list using index slicing.

print("---------------------------------------------------------------------------------")
15). Python program to reverse a list with reversed and reverse methods.

print("---------------------------------------------------------------------------------")
16). Python program to copy or clone one list to another list.

print("---------------------------------------------------------------------------------")
17). Python program to return True if two lists have any common member.

print("---------------------------------------------------------------------------------")
18). Python program to print a specific list after removing the 1st, 3rd, and 6th elements from the list.

print("---------------------------------------------------------------------------------")
19). Python program to remove negative values from the list.

print("---------------------------------------------------------------------------------")
20). Python program to get a list of all elements which are divided by 3 and 7.

print("---------------------------------------------------------------------------------")
21). Python program to check whether the given list is palindrome or not. (should be equal from both sides).

print("---------------------------------------------------------------------------------")
22). Python Program to get a list of words which has vowels in the given string.
Input: “www Student ppp are qqqq learning Python vvv”
Output : [‘Student’, ‘are’, ‘learning’, ‘Python’]
print("---------------------------------------------------------------------------------")

23). Python program to add 2 lists with extend method.

print("---------------------------------------------------------------------------------")
24). Python program to sort list data, with the sort and sorted method.

print("---------------------------------------------------------------------------------")
25). Python program to remove data from the list from a specific index using the pop method.

print("---------------------------------------------------------------------------------")
26). Python program to get the max, min, and sum of the list using in-built functions.

print("---------------------------------------------------------------------------------")
'''