'''
1.In list we can store homogenous and heterogeneous type of data
2.In List we can store duplicate values
3.List is ordered collection of data: order of insertion will remain as it is in the output.
4.Lists are Mutable: Once we declare the list we can modify it.
'''
li1 = [10,20,30,40.45,True,'Kodnest',20]
print(li1,type(li1))

#append():will add element at the end of the list.
li1.append(300)
print(li1)

#insert(index,element):insert element at a paticular index
li1.insert(1,15)
print(li1)

#remove():removes the first occurnce of the specified ele.
li1.remove(20)
print(li1)


#in and not in Operator:
print(2000 in li1)
print('Kodnest'  in li1)

#pop():without argument will delete and return last ele. from list
removed_ele = li1.pop()
print(removed_ele)
print(li1)

removed_ele = li1.pop(4)
print(removed_ele)
print(li1)