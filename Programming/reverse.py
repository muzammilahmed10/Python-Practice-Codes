#iterable_obj.reverse() method will reverse the original objects
li  = [10,5,20,7,40]
print('Before Reverse',li)
li.reverse()
print('After Reverse',li)#After Reverse [40, 7, 20, 5, 10]

#reversed(iterable_objcet):
li1 = [10,20,30,40,50]
reversed_li1 = list(reversed(li1))
print(li1) #[10, 20, 30, 40, 50]
print(reversed_li1)#[50, 40, 30, 20, 10]

li3 = [1,5,2,9]
new_reverse_li3 = list(reversed(li3)) #-->Creating new reverse list
li3.reverse()#-->Reversing original list
print(new_reversed_li3)
