n=int(input())
p=[list(map(int,input().split())) for i in range(n)]
ans=0
for i in range(n):
    for j in range(i+1,n):
        ans+=(abs(p[j][0]-p[i][0])>=abs(p[j][1]-p[i][1]))
print(ans)