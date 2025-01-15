rows = 5
col = 5
for i in range(rows):
    for j in range(col):
        print('*',end='')
    print()
#upward right angle triangle
for i in range(rows):
    for j in range(i+1):
        print('*',end=' ')
    print()
print()
#downward riht angle triangl
for i in range(rows):
    for j in range(rows-i):
        print('*',end=' ')
    print()
#right pascle triangle
for i in range(rows-1):
    for j in range(i+1):
        print('*',end=' ')
    print()

for i in range(rows):
    for j in range(i,rows):
        print('*',end=' ')
    print()
print()

for i in range(rows):
    for j in range(i+1):
        print('*',end='')
    for j in range(i,rows-1):
        print(' ',end="")
    for j in range(i,rows-1):
        print('',end="")
    for j in range(i+1):
        print('*',end='')
    print()

for i in range(rows):
    for j in range(i,rows-1):
        print('*',end='')
    for j in range(i+1):
        print('',end="")
    for j in range(i+1):
        print(' ',end="")
    for j in range(i,rows-1):
        print('*',end='')
    print()

print()
for i in range(rows):
    for j in range(i,rows):
        print(' ',end='')
    for j in range(i):
        print("*",end='')
    for j in range(i+1):
        print("*",end='')
    print()

for i in range(rows):
    for j in range(i+1):
        print(' ',end='')
    for j in range(i,rows-1):
        print("*",end='')
    for j in range(i,rows):
        print("*",end='')
    print()
