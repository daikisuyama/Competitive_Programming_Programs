n=int(input())
s=list(map(int,input()))
t=list(map(int,input()))
ans=0
s0,t0=s.count(0),t.count(0)
if s0>t0 or s0%2!=t0%2:
    print(-1)
    exit()
from bisect import bisect_left
sind=[i for i in range(n) if s[i]==0]
tind=[i for i in range(n) if t[i]==0]
ls,lt=len(sind),len(tind)
check=[0]*ls
for i in range(ls):
    check[i]=bisect_left(tind,sind[i])
print(check)
for i in range(ls-1,-1,-1):
    ch=tind[-(ls-i)]-sind[i]
    if ch<0:
        print(-1)
        exit()
    ans+=ch
if ls==lt:
    print(ans)
    exit()
#残りを変える(偶数個)
tr=tind[lt-ls-1]
s_=[1]*(tr+1)
for i in range(1,tr+1):
    if s_[i-1]!=t[i-1]:
        s_[i-1]=t[i-1]
        s_[i]=0
        ans+=1
print(ans)

