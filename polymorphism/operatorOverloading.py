class Demo1:
    def __init__(self):
        self.a = 20
    def disp1(self):
        print("Inside disp1")
    def __str__(self):
        return 'Hello'
    def __add__(self,other):
        self.a = 10
        other.b = 20
        return self.a+other.b
class Demo2:
    def disp2(self):
        print("Inside disp2")
    def __str__(self):
        return 'Hii'
d1 = Demo1()
d2 = Demo2()
print(d1)
print(d2)
print(d1+d2)
 #In pytho if we print refrence valriable then internally python will invoke __str__() which always returns string represntation of address of an object.
 #In the above examples we have overriden __str__ methods in their respective classes
