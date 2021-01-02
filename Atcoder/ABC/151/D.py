h,w=map(int,input().split())
s=[list(input()) for i in range(h)]
inf=1000000000
wf=[[inf]*(h*w) for i in range(h*w)]
for i in range(h*w):
    k,l=i//w,i%w
    #print(l)
    if s[k][l]=="#":
        continue
    if k!=0:
        if s[k-1][l]==".":
            wf[i][i-w]=1
    if k!=h-1:
        if s[k+1][l]==".":
            wf[i][i+w]=1
    if l!=0:
        if s[k][l-1]==".":
            wf[i][i-1]=1
    if l!=w-1:
        if s[k][l+1]==".":
            wf[i][i+1]=1
    wf[i][i]=0
for i in range(h*w):
    for j in range(h*w):
        for k in range(h*w):
            wf[j][k]=min(wf[j][k],wf[j][i]+wf[i][k])
ans=0
for i in range(h*w):
    for j in range(h*w):
        if wf[i][j]!=inf:
            ans=max(ans,wf[i][j])
print(ans)