class Demo1:
    def __init__(self):
        self.x = 100
    def __init__(self):
        self.x = 200
d1 = Demo1()
print(d1.x)


'''
When we create multiple constructors in the same class then only last declared constructor will be invoked at the object creation.python does not support constructor overloading
'''