h,w=map(int,input().split())
ran=[[j-1 for j in list(map(int,input().split()))] for i in range(h)]
cand=[]
if ran[0][0]>1:
    cand.append(0)
    cand.append(ran[0][0]-1)
elif ran[0][0]==1:
    cand.append(ran[0][0]-1)
if ran[0][1]<w-2:
    cand.append(w-1)
    cand.append(ran[0][1]+1)
elif ran[0][1]==w-2:
    cand.append(ran[0][1]+1)
cand=list(range(w))
dp=[[[-1,-1] for j in range(h+1)] for i in range(len(cand))]
ans=[-1]*h
for i in range(len(cand)):
    dp[i][0]=[cand[i],0]
    for j in range(h):
        if dp[i][j][0]<ran[j][0]:
            if ran[j][0]==0:
                break
            else:
                dp[i][j+1]=[dp[i][j][0],dp[i][j][1]+1]
        elif dp[i][j][0]<=ran[j][1]:
            if ran[j][1]==w-1:
                break
            else:
                dp[i][j+1]=[ran[j][1]+1,dp[i][j][1]+(ran[j][1]-dp[i][j][0]+1)+1]
        else:
            dp[i][j+1]=[dp[i][j][0],dp[i][j][1]+1]
    for j in range(h):
        if dp[i][j+1][1]!=-1:
            if ans[j]!=-1:
                ans[j]=min(ans[j],dp[i][j+1][1])
            else:
                ans[j]=dp[i][j+1][1]
for i in range(h):
    print(ans[i])