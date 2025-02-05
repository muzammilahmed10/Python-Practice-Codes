from abc import ABC, abstractmethod
class Demo1(ABC):
    # @abstractmethod
    # def disp1(self):
    #     print('Inside Disp1')
    pass


'''
If abstract class Doesnt have any method then object for that abstract class can be created.
'''
class Demo2(ABC):
    def disp2(self):
        print('Inside disp2')

d2 = Demo2()
d2.disp2()
'''
If abstract class have only concrete method then object for tht abstract class can be created and concrete methods can be invoked.
'''

class Demo3(ABC):
    @abstractmethod
    def disp3(self):
        print('Inside disp3')
class Demo4(Demo3):
    pass
d4 = Demo4()