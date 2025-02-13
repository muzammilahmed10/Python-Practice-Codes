li = [1,2,3,4]

def double(num):
    return num * 2

double_li = list(map(double,li))
print(double_li)

def even(num):
    return num % 2 == 0
        
filter_li = list(filter(even,li))
print(filter_li)

def multiply(x,y):
    return x*y
from functools import reduce
reduce_li = reduce(multiply,li)
print(reduce_li)
