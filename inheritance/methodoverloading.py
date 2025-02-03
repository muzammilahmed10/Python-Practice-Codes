class Demo:
    def disp(self):
        print("inside disp1 with 0 para")
    def disp(self,a):
        print('inside disp with one para')
    def disp(self,a,b):
        print("inside disp with two para")

d = Demo()
# d.disp()
# d.disp(10)
d.disp(10,20)
    