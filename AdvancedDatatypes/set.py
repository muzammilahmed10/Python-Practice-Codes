'''
1.In set we can store Homogenous as well as Heterogeneous Data
2.Set is an unordered collection of data
3.Set does not support indexing of data
4.In sets we cannot store duplicates
5.Sets are mutable
'''

s1 = {10,True,'kodnest',10,20,55.44}
print(s1,type(s1))#{True, 'kodnest', 20, 55.44, 10} <class 'set'>

#add():
s1.add(50)
print(s1)#{True, 50, 20, 55.44, 'kodnest', 10}

s1.remove(55.44)
print(s1)#{True, 50, 20, 'kodnest', 10}   

#pop():Withut index will delete and return one ele.
poped_ele=s1.pop()
print(poped_ele)#True
print(s1)#{50, 20, 10, 'kodnest'}

print(2000 in s1)#False