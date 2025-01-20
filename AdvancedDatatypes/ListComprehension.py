li1 = [1,2,3,4,5]
sq_li = []
for i in li1:
   sq_li.append(i**2)

print(sq_li)

li2 = [1,2,3]
new_li = [ i for i in li2]
print(li2)
sq_li1 = [i**2 for i in li2]
print(sq_li1)

#when we have only if part then write it afer for loop.
even = [i for i in li2 if i%2==0]
print(even)

#when we have if-else both write it before for loop
even_odd = ['even' if i%2==0 else 'Odd' for i in li2]
print(even_odd)






#nested for loops inside list comprehension
li = [[10,20],[30,40],[50,60]]
new_li = [ele for sublist in li for ele in sublist]
print(new_li)