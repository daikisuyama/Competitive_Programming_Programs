n=int(input())
b=list(map(int,input().split()))
if n==1 or n==2:
    print(0)
    exit()
inf=10**12
#x,yはchangeの量(0,-1,+1),9通り
def check(x,y):
    global b,n
    ret=0
    if x!=0:
        ret+=1
    if y!=0:
        ret+=1 
    a=[i for i in b]
    a[0]+=x
    a[n-1]+=y
    #昇順に
    if a[n-1]<a[0]:
        a=a[::-1]
    if (a[n-1]-a[0])%(n-1)!=0:
        return inf
    d=(a[n-1]-a[0])//(n-1)
    for i in range(n-1):
        if a[i+1]-a[i]==d:
            pass
        elif a[i+1]-a[i]==d+1:
            a[i+1]-=1
            ret+=1
        elif a[i+1]-a[i]==d-1:
            a[i+1]+=1
            ret+=1
        else:
            return inf
    return ret

ans=inf
for i in range(-1,2):
    for j in range(-1,2):
        ans=min(ans,check(i,j))
        #print(i,j,check(i,j))
if ans==inf:
    print(-1)
else:
    print(ans)