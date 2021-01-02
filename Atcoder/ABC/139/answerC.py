n=int(input())
h=[int(i) for i in input().split()]
c=0
d=c
for i in range(n-1):
    if h[i]>=h[i+1]:
        c+=1
    else:
        d=max([c,d])
        c=0
    if i==n-2:
        d=max([c,d])

print(d)
