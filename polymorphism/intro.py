#This code use to provide the achievement of polymorphis using method overriding
class Calculator:
    def calculat(self,a,b):
        pass
class Add(Calculator):
    def calculat(self,a,b):
        print('Addition: ',a+b)
class Sub(Calculator):
    def calculat(self,a,b):
        print('Subtraction: ',a-b)
class Mul(Calculator):
    # def calculat(self,a,b):
    #     print('Multiplication:',a*b)
    pass
ref = Add()
ref.calculat(10,20)

ref = Sub()
ref.calculat(20,10)

ref = Mul()
ref.calculat(20,10)