li = []
n = int(input())
for i in range(n):
    name = input()
    score = float(input())
    li.append([name,score])
scores = []
for name,score in li:
    scores.append(score)
    scores = list(set(scores))
    scores.sort()
nameli = []
second_smallest = scores[1]
for name,score in li:
     if score == second_smallest:
       nameli.append(name)
nameli.sort()
#print("=============================")
for name in nameli:
    print(name)