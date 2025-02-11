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