'''
1.dictionary can store homogeneous as well as heterogeneous type of data
2.In dict we cannot store duplicate keys but can store duplicate values
3.Dict is mutable
'''
d1 = {'name':'Priya','age':27,'phone':234567}
print(d1,type(d1))#{'name': 'Priya', 'age': 27, 'phone': 234567} <class 'dict'>

d1['name'] = 'Pooja'
print(d1)#{'name': 'Pooja', 'age': 27, 'phone': 234567}

for i in d1.keys():
    print(i)
for i in d1.values():
    print(i)
for i in d1.items():
    print(i)