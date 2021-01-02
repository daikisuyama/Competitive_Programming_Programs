n,r=map(int,input().split())
s=list(input())
if s=="o"*n:
    print(0)
    exit()
ans=0
now=n-1
for i in range(n-1,-1,-1):
    if s[i]==".":
        for j in range(i,max(i-r,-1),-1):
            s[j]="o"
        ans=max(i-r,-1)+2
        now=i-1
        break
#print(ans)
while True:
    #print(now)
    if now==-1:
        print(ans)
        break
    if s[now]==".":
        for j in range(now,max(now-r,-1),-1):
            s[j]="o"
        ans+=1
        now=max(now-r,-1)
    else:
        now-=1