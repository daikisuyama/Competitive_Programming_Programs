n,m=map(int,input().split())
ab=[list(map(int,input().split())) for i in range(m)]
ab.sort(key=lambda x:x[1])
ans=[[ab[0][1]-1,ab[0][1]]]
ab.pop(0)
for i in range(m-1):
    if ans[-1][0]>=ab[i][0]:
        continue
    else:
        ans.append([ab[i][1]-1,ab[i][1]])
print(len(ans))