
'''dict1 = {'a':12, 'b':4, 'c':11, 'd':8}

for k,v in dict1.items():
    print(k,v)
dict1['e']=6
dict1['f']=9

print(dict1)
print(dict1.items())
print("-----------------------------------------------------------------------------------------")
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
print("-----------------------------------------------------------------------------------------")
dict_3 = {}
for v in range(0,10):
    if v%2 == 0:
        dict_3[v] = v**2
    else:
        continue
print(dict_3)
print("-----------------------------------------------------------------------------------------")

dict_4 = {'a':4, 'b':5, 'c':6, 'd':8, 'e':7}
dict_5 = {'f':"a", 'j':"b", 'k':"c", 'l':"d", 'm':"e"}

dict_4.update(dict_5)
print("after added 5 in to 4:", dict_4)
print("-----------------")

val = dict_4.pop('k')
print("removed value:", val)
print("after removed a value:", dict_4)

print("-----------------------------------------------------------------------------------------")

list1 = [9,8,7,6,5,4]
list2 = {"p","o","i","u","y","t"}

tuple1 = (1,2,3,4,5)
tuple2 = ("a","b","c","d","e")

dict_6 = dict(zip(list1, list2))
print(dict_6)

dict_7 = dict(zip(tuple1, tuple2))
print(dict_7)

print("-----------------------------------------------------------------------------------------")

# Get data from dict ###

from pprint import pprint

office = {
    'team_dev':
        { 'sr_dev': { 'tm1':["suresh", "naresh", "ramesh"], 'tm2':["hari", "bery", "chery"] } ,
          'jr_dev': { 'tma':["ar", "br", "cr"], 'tmb':["ba", "ca", "ma"] } } ,

    'team_test':
        { 'sr_test': {'tsa':(1,2,3), 'tsb':(4,5,6) } ,
          'jr_test': {'ts1':(7,8,9), 'ts2':(10,11,12) } } ,

    'team_it':
        { 'sup': ["b1", "b2", "b3"], 'hlp': ["a1", "a2", "a3"] } ,

    'team_mgm':
        { 'manager1': (11,22,33), 'manager2': (44,55,66) }
       }

pprint(office)

print("-----------------------------------------------------------------------------------------")
'''