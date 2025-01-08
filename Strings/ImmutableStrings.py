""" Strings are immutable 
1.Once we declare the String we cannot modify it, if we try to modify the String it will create new String.
"""
# s1 = 'Kodnest'
# s1.upper()
# print(s1)

# s1 = 'K'
# print(s1,id(s1))

s1 = 'Hello'
s2 = 'World'
print(s1,id(s1))
print(s2,id(s2))
print(s1[0])
print(s1[-1])
print('s1 id of H',id(s1[0]))
print('s1 id of o',id(s1[-1]))
print('s2 ID of o:',id(s2[-1]))
print('s2 ID of W:',id(s2[0]))


print('s1 ID of l:',id(s1[2]))
print('s1 id of l:',id(s1[3]))
print('s1 id od l:',id(s2[3]))