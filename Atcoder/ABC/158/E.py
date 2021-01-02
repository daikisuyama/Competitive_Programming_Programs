from itertools import groupby
n,p=map(int,input().split())
s=[int(i) for i in input()]
if p==2 or p==5:
    ans=0
    for i in range(n-1,-1,-1):
        #Rとなるもの
        if s[i]%p==0:
            ans+=(i+1)
    exit(print(ans))
S=[0]*(n+1)
po=[1]*(n+1)
for i in range(n):
    po[i+1]=po[i]*10
    po[i+1]%=p
for i in range(n-1,-1,-1):
    S[i]=S[i+1]+s[i]*po[n-1-i]
    S[i]%=p
t=[[S[i],i] for i in range(n+1)]
t.sort()
#[L,R)となるのの候補
#ここ普通にmapでよくねーか
u=[[i[1] for i in sorted(list(group))] for key,group in groupby(t,key=lambda x: x[0])]
ans=0
for v in u:
    ans+=(len(v))*(len(v)-1)//2
print(ans)