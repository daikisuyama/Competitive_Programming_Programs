n,x,m=map(int,input().split())
cand=[x]
cands=set()
cands.add(x)
for i in range(m):
    c=(cand[-1]**2)%m
    if c in cands:
        break
    else:
        cand.append(c)
        cands.add(c)
#ループの初め
#print(cand)
p=cand.index(c)
if x<p:
    print(sum(cand[:x]))
    exit()
ans=sum(cand[:p])
cand=cand[p:]
#print(ans)
n-=p
#ループの回数
tim=n//len(cand)
ama=n%len(cand)
ans+=tim*sum(cand)
ans+=sum(cand[:ama])
print(ans)
#print(p)
#print(cand)