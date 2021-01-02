n=int(input())
l=sorted([int(i) for i in input().split()])
c=0
for i in range(n):
    c+=l[2*i]
print(c)
