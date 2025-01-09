print(bool('kodnest'))#true
#print(int('kod'))#error
print(int('11'))#11
#print(float('kodnest'))#error
print(float('22.22'))#22.22
print(bool(''))#false
print(bool(0))#false
print(bool(12))#true
#print(int('12.56'))#error
print(int(12.56))#12

#Taking float value from user and converting it into int
value  = int(float(input('enter price: float value')))
print(value,type(value))