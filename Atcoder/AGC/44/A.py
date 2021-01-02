import math
#xはstr
def changeton(x,k):
    ret=[]
    while x!=0:
        ret.append(x%k)
        x=x//k
    return ret[::-1]

def answers(n,y,d,m):
    x=changeton(n,m)
    ans=0
    for j in range(len(x)):
        zj=x[j]
        if j==len(x)-1:
            ans1,ans2=ans+(m-zj),ans+zj
            ans=min(len(x)*y+ans1*d,(len(x)-1)*y+ans2*d)
            continue
        if zj>=3:
            ans+=(m-zj)
            x[j+1]+=1
        else:
            ans+=zj
    return ans


t=int(input())
for i in range(t):
    n,a,b,c,d=map(int,input().split())
    print([answers(n,a,d,2),answers(n,b,d,3),answers(n,c,d,5)])