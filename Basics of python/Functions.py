#without input and withouT RETURN stmt
def add():
    a = 10
    b = 20
    print('Addition is:',a+b)

#with input and without return stmt
def sub(a,b):
    print('Substraction is:',a-b)

#without input and with return stmt:
def mul():
    return 10*20

#with input and with return stmt
def div(a,b):
    return a/b

add()
sub(100,50)
print(mul())
print(div(200,10))