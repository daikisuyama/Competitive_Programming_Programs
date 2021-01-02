n=int(input())
a=list(map(int,input().split()))
b=0
for i in range(n):
    b^=a[i]
ans=[0]*n
for i in range(n):
    ans[i]=a[i]^b
print(" ".join(map(str,ans)))