n=int(input())
xy=[list(map(int,input().split())) for i in range(n)]
ans=[]
cand=[xy[i][0]+xy[i][1] for i in range(n)]
ans.append(max(cand)-min(cand))
cand=[-xy[i][0]+xy[i][1]for i in range(n)]
ans.append(max(cand)-min(cand))
cand=[-xy[i][0]-xy[i][1] for i in range(n)]
ans.append(max(cand)-min(cand))
cand=[xy[i][0]-xy[i][1] for i in range(n)]
ans.append(max(cand)-min(cand))
print(max(ans))