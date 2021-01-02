import bisect
n=int(input())
a=[int(i) for i in input().split()]
b=[0]*(10**5)
for i in range(n):
    b[a[i]]+=1
ma=0
for i in range(1,10**5-1):
    ma=max(b[i-1]+b[i]+b[i+1],ma)
print(ma)
#はじめにチェックしておく
