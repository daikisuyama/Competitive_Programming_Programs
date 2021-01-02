n,d,m=map(int,input().split())
a=list(map(int,input().split()))
e,f=[i for i in a if i<=m],[i for i in a if i>m]
e.sort(reverse=True)
f.sort(reverse=True)
c=len(e)
if c==n:
    print(sum(a))
    exit()
#a[i]>mはmaxまで適当に選べる
l=1
r=min((n-1)//(d+1)+1,len(f))
#k's range 
#e,f 's sum
ans=sum(e)
nowe,nowf=0,0
for i in range(l,r+1):
    if i==l:
        nowe=sum(e[:n-(1+(l-1)*(d+1))])
        nowf=sum(f[:l])
        ans=max(nowe+nowf,ans)
        continue
    nowe-=sum(e[n-(1+(i-1)*(d+1)):n-(1+(i-1-1)*(d+1))])
    nowf+=f[i-1]
    ans=max(nowe+nowf,ans)
print(ans)