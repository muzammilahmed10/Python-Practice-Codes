'''
In tuples we can store homogenous as well as heterogenous type of data
In tuples we can store Duplicates.
Tuples are ordered collection of data
Tuples are immutable: once we declare the tuple we cannot modify it.
'''
tup1 = (10,22.5,'Kodnest',True,10)
print(tup1)
#tup1.append(400)

t1 = (1,2,3)
t2 = (4,5,6)
t3 = t1+t2
print(t3)

#Create a singleton tuple:
tup = (10,)
print(tup,type(tup))#(10,) <class 'tuple'>

