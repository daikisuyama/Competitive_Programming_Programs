x,n=map(int,input().split())
p=sorted(list(map(int,input().split())))
q=[0]*(102)
for i in range(n):
    q[p[i]]=1
ans=(1000000,-1)
for i in range(102):
    if q[i]==0:
        if ans[0]>abs(i-x):
            ans=(abs(i-x),i)
print(ans[1])