import bisect
n=int(input())
a=[int(input()) for i in range(n)]
b=list(set(a))
b.sort()
c=[0]*n
for i in range(n):
    c[i]=bisect.bisect_left(b,a[i])
for i in range(n):
    print(c[i])
