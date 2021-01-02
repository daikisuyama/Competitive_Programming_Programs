from math import gcd
def gce(x):
    ret=x[0]
    for i in x:
        ret=gcd(ret,i)
    return ret
n=int(input())
a=list(map(int,input().split()))
g=gce(a)
a=[i//g for i in a]
b=[]
for i in range(n):
    d=[0,0]
    c=a[i]
    while c%2==0:
        c//=2
        d[0]+=1
    while c%3==0:
        c//=3
        d[1]+=1
    b.append(d)
b.sort(key=lambda x:x[0])
b.sort(reverse=True,key=lambda x:x[1])
ans=[]
for i in range(n):
    ans.append(str((2**b[i][0])*(3**b[i][1])*g))
print(" ".join(ans))