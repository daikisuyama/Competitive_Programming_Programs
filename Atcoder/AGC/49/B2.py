n=int(input())
s=list(map(int,input()))
t=list(map(int,input()))
s0,t0=s.count(0),t.count(0)
if s0>t0 or s0%2!=t0%2:
    print(-1)
    exit()
sind=[i for i in range(n) if s[i]==0]
tind=[i for i in range(n) if t[i]==0]
ls,lt=len(sind),len(tind)
for i in range(ls-1,-1,-1):
    ch=tind[-(ls-i)]-sind[i]
    if ch<0:
        print(-1)
        exit()
ans=0
now=n-1
while True:
    if s[now]==t[now]:
        if s[now]==0:
            ls-=1
            lt-=1
        now-=1
        continue
    if ls==lt:
        break
    if now<3:
        break
    if (s[now]==1 and s[now-1]==1)and(t[now]==0 and t[now-1]==0)and(not(s[now-2]==0 and t[now-2]==1)):
        ans+=1
        now-=2
        lt-=2
    else:
        break
sind=sind[:ls]
tind=tind[:lt]
for i in range(ls-1,-1,-1):
    ch=tind[-(ls-i)]-sind[i]
    ans+=ch
if ls==lt:
    print(ans)
    exit()
tr=tind[lt-ls-1]
s_=[1]*(tr+1)
for i in range(1,tr+1):
    if s_[i-1]!=t[i-1]:
        s_[i-1]=t[i-1]
        s_[i]=0
        ans+=1
print(ans)

