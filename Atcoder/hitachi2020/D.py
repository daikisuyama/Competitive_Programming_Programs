n,t=map(int,input().split())
ab=[list(map(int,input().split())) for i in range(n)]
ab.sort(key=lambda x:x[0]+x[1])

def countk(k):
    global ab,n,t
    ret=0
    ab_=sorted(ab[:k],key=lambda x:x[0],reverse=True)
    for i in range(k):
        ret+=1
        ret=ret+ab_[i][0]*ret+ab_[i][1]
    return ret

l,r=0,n
while l+1<r:
    k=(l+r)//2
    if countk(k)<=t:
        l=k
    else:
        r=k
#print(r)
#print(countk(r))
if countk(r)<=t:
    print(r)
else:
    print(l)