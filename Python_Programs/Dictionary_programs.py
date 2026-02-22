
'''dict1 = {'a':12, 'b':4, 'c':11, 'd':8}

for k,v in dict1.items():
    print(k,v)
dict1['e']=6
dict1['f']=9

print(dict1)
print(dict1.items())

dict_2 = "Welcome to kagaznagar and its my home town"
result={}
num = 0
val = dict_2.split(" ")
print(val)
for w in val:
    print(w)
    num = num+1
    x = (num)
    result[x] = w
    print(result)
print(result)
'''

dict_3 = {}
for v in range(0,10):
    if v%2 == 0:
        dict_3[v] = v**2

    else:
        continue
print(dict_3)