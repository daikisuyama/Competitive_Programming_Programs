w,h=map(int,input().split())
cost=[]
for i in range(w):
    p=int(input())
    cost.append([p,i,0])
for i in range(h):
    q=int(input())
    cost.append([q,i,1])
cost.sort()
#行,列方向の情報がきたときに繋げる必要のある本数
ans=0
check=[w+1,h+1]
for c,ind,t in cost:
    #行方向の情報
    if t:
        ans+=check[0]*c
        check[1]-=1
    #列方向の情報
    else:
        ans+=check[1]*c
        check[0]-=1
print(ans)