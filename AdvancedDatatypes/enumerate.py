# li = [10,20,30]
# for idx,ele in enumerate(li):
#     print(idx,ele)

#Write a python prog to print all even index ele

li = [10,20,30,40,50]
for idx,ele in enumerate(li,start=1):
    if idx %2==0:
        print(idx,ele)