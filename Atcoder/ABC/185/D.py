from math import gcd
n,m=map(int,input().split())
a=[0]+list(map(int,input().split()))+[n+1]
a.sort()
#連続してないとこは含める
#連続してるところは飛ばす
cand=[]
for i in range(m+1):
    if a[i+1]-a[i]==1:
        continue
    else:
        cand.append(a[i+1]-a[i]-1)
if len(cand)==0:
    print(0)
    exit()
g=cand[0]
for i in range(1,len(cand)):
    g=min(g,cand[i])
#print(g)
ans=0
for i in cand:
    ans+=(-(-i//g))
print(ans)