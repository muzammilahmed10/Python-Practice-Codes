import time
li1 = [1,2,3,4,5]
li2 = ['a','b','c','d','e']

def displayDigits(li1):
    for i in li1:
        print(i)
        time.sleep(1)
def displayAlphabets(li2):
    for i in li2:
        print(i)
        time.sleep(1)
d = displayDigits(li1)
a = displayAlphabets(li2)
print(d)
print(a)