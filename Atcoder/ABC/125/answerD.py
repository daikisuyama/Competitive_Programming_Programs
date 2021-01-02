n=int(input())
a=[int(i) for i in input().split()]
a.sort()
j=n
for i in range(n):
    if a[i]>=0:
        j=i
        break
a=list(map(abs,a))
a.sort()
if j%2==0:
    print(sum(a))
else:
    print(sum(a)-2*a[0])
