s = input()
p,c = input().split()

def mutation(s,p,c):
    li = list(s)
    li[p] = c
    res=''.join(li)
    return res
print(mutation(s,int(p),c))