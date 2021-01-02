from sys import exit
def groupby(a):
    a2=[[a[0],1]]
    for i in range(1,len(a)):
        if a2[-1][0]==a[i]:
            a2[-1][1]+=1
        else:
            a2.append([a[i],1])
    return a2

n,k=map(int,input().split())
s=list(input())
x=groupby(s)
l=len(x)
y=[x[i][1] for i in range(l)]

if x[0][0]=="0":
    su=sum(y[:2*k])
    ans=su
    y.pop(0)
    l-=1
else:
    ans=0
su=sum(y[:2*k+1])
ans=max(ans,su)
l_sub=(l-(2*k+1))//2
if l_sub<=0:
    print(ans)
    exit()
for i in range(l_sub):
    su-=y[2*i]
    su-=y[2*i+1]
    su+=y[2*k+1+(2*i)]
    su+=y[2*k+1+(2*i+1)]
    ans=max(su,ans)
#最後のところの判定っぽいな
if 2*k+1+2*l_sub<l:
    su-=y[2*l_sub]
    su-=y[2*l_sub+1]
    su+=y[2*k+1+2*l_sub]
    ans=max(su,ans)
print(ans)
