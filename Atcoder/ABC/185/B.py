n,m,t=map(int,input().split())
ab=[list(map(int,input().split())) for i in range(m)]
now=n
where=0
#減って増える,最後のカウントも
for i in range(m):
    now-=(ab[i][0]-where)
    if now<=0:
        print("No")
        break
    now=min(n,now+ab[i][1]-ab[i][0])
    where=ab[i][1]
else:
    now-=(t-where)
    if now<=0:
        print("No")
    else:
        print("Yes")