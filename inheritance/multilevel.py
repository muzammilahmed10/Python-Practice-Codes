class Demo1:
    def disp(self):
        print("inside disp1")

class Demo2(Demo1):
     def disp2(self):
        print("inside disp2")

class Demo3(Demo2):
    pass
    
d3 = Demo3()
d3.disp()
d3.disp2()