n=int(input())
a=[i for i in input().split()]

b=[]
c=[]
if n%2==0:
    for i in range(n):
        if i%2==0:
            b.append(a[i])
        else:
            c.append(a[i])
else:
    for i in range(n):
        if i%2==0:
            c.append(a[i])
        else:
            b.append(a[i])
c=c[::-1]
print(" ".join(c)+" "+" ".join(b))
