n=int(input())

a1=list(map(int,input().split()))
b=list(map(int,input().split()))
a2=sorted(a1)
b.sort()

for i in range(n):
    if b[i]<a2[i]:
        s="No"
        break
else:
    s="Yes"

for i in range(n-1):
    a2[-1-i],a2[-2-i]=a2[-2-i],a2[-1-i]
if a1==a2:
    s="No"

print(s)
