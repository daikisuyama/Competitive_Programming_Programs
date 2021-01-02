n,m=map(int,input().split())
ps=[list(input().split()) for i in range(m)]
pen=[0]*n#ペナ数
rig=[0]*n#ACorWA

for i in range(m):
    if ps[i][1]=="AC":
        rig[int(ps[i][0])-1]=1
    else:
        if rig[int(ps[i][0])-1]==0:
            pen[int(ps[i][0])-1]+=1
cnt1,cnt2=0,0
for i in range(n):
    if rig[i]==1:
        cnt1+=rig[i]
        cnt2+=pen[i]
#print(pen)
print(str(cnt1)+" "+str(cnt2))