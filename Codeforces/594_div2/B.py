n=int(input())
a=list(map(int,input().split()))
a.sort()
c,d=0,0
for i in range(n//2):
    c+=a[i]
for i in range(n//2,n):
    d+=a[i]
print(c**2+d**2)