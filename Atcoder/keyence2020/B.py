n=int(input())
sec=[list(map(int,input().split())) for i in range(n)]
for i in range(n):
    sec[i][0]+=sec[i][1]
    sec[i][1]*=-2
    sec[i][1]+=sec[i][0]
sec.sort()

ans=0
#-inf
t=-10000000000
for i in range(n):
    #=をつけるのを忘れずに
    if t<=sec[i][1]:#スタートがロボットアームのある最大の座標以上でなければならない
        ans+=1#以上なら+1
        t=sec[i][0]#ロボットアームのある最大の座標を更新
print(ans)
