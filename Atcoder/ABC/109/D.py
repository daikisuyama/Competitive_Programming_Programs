h,w=map(int,input().split())
a=[list(map(int,input().split())) for i in range(h)]
ans=[]
for i in range(h):
    for j in range(w-1):
        if a[i][j]%2==1:
            a[i][j+1]+=1
            a[i][j]-=1
            ans.append([i+1,j+1,i+1,j+2])
for i in range(h):
    if a[i][w-1]%2==1:
        if i!=h-1:
            a[i+1][w-1]+=1
            a[i][w-1]-=1
            ans.append([i+1,w,i+2,w])
l=len(ans)
print(l)
for i in range(l):
    print(" ".join(map(str,ans[i])))