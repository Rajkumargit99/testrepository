import random

var = random.randint(1, 20)
print(var)
print("-------------------------------------")

var2 = random.choice([1,4,9,20,40])
print(var2)
print("-------------------------------------")

var3 = [2,5,6,"hi", {2,5}, (1,4,3)]
result = random.shuffle(var3)
print(var3)