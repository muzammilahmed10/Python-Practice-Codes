def disp():
    return 10
    return 20
    return 30
res = disp()
print(res)#10
print(disp())#10
print(disp())#10

def generator_function():
    yield 10
    yield 20
    yield 30
gen = generator_function()
print(next(gen))#10
print(next(gen))#20
print(next(gen))#30

def fibonacci(n):
    a,b = 0,1
    for i in range(n):
        print(a)
        a,b = b,a+b
fibonacci(10)

def fibonacci_gen(n):
    a,b = 0,1
    for i in range(n):
        yield a
        a,b = b,a+b
ref = fibonacci_gen(10)

for i in range(5):
    print(next(ref))


#https://github.com/Priya9096/Python-Practice-Codes/tree/main/Solutions