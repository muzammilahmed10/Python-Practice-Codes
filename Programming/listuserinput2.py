# li = input('Enter space seperated Elements')
# print(li,type(li))
# li = li.split()
# print(li)#['3', '4', '5']  --.> split() func converts the elements persent with spaces into single list

# li = list(map(int,li))
# print(li) #[3, 4, 5]

# tup = tuple(map(int,input('Enter space seperated elements').split()))
# print(tup)

li = map(int,input().split())
print([i for i in li if i %2==0])

