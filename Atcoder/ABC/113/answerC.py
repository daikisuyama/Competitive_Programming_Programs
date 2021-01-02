n,m=map(int,input().split())
pyi=[[] for i in range(n)]
for i in range(m):
    p,y=map(int,input().split())
    pyi[p-1].append([y,i])
ans=[]
for i in range(n):
    pyi[i].sort()
    for j in range(len(pyi[i])):
        ans.append([(6-len(str(i+1)))*"0"+str(i+1)+(6-len(str(j+1)))*"0"+str(j+1),pyi[i][j][1]])
ans.sort(key=lambda x:x[1])
for i in range(m):
    print(ans[i][0])