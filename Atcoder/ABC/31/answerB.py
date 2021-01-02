l,h=[int(i) for i in input().split()]
n=int(input())
a=[]
for i in range(n):
    b=int(input())
    if b<=l:
        a.append(l-b)
    elif b<=h:
        a.append(0)
    else:
        a.append(-1)
for i in range(n):
    print(a[i])
