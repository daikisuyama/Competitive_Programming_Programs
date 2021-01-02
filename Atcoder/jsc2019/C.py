n=int(input())
s=input()
if s[0]=="W":
    exit(print(0))
t=[1]
for i in range(1,2*n):
    if s[i]==s[i-1]:
        t.append(-t[-1])
    else:
        t.append(t[-1])
now=1
for i in range(1,2*n):
    now+=t[i]
    if now<0:
        exit(print(0))
if now!=0:
    exit(print(0))
#左は確実に余ってるので右がきたら組み合わせる方向性で
ans=1
mod=10**9+7
ca=0
for i in range(2*n):
    if t[i]==1:
        ca+=1
    else:
        ans*=ca
        ans%=mod
        ca-=1
#この時点のansは組み合わせの数のみその順番を考慮していない
for i in range(1,n+1):
    ans*=i
    ans%=mod
print(ans)