'''
1. Conditional : if-else,if-elif
2. loofing: for,while
3. jumping: break,continue,pass 
'''
def checkAge(age):
    if(age>18):
        print('Age is greater than 18')
    else :
        print('Age is not greater than 18')
checkAge(18)

#WAP to display 'Child' if age is below 18, display 'Adult  is age is above 18, display senior citizen if age above 65.

def checkAge1(age):
    if(age<18):
        print('Child')
    elif(age>=18):
        print('Adult')
    else:
        print('Senior citizen')
checkAge1(60)