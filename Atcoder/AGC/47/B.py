n=int(input())
ss=[input() for i in range(n)]
m=dict()
def chi(x):
    return ord(x)-ord("a")
#それぞれの文字列のi文字目までの種類
#set→整数
check=[[0 for j in range(len(ss[i]))]for i in range(n)]
for i in range(n):
    check[i][0]=1<<chi(ss[i][0])
    for j in range(1,len(ss[i])):
        check[i][j]=check[i][j-1]|(1<<chi(ss[i][j]))
#m[s][i]:0or1
#mapも整数に(あるかどうかなので)
for i in range(n):
    if ss[i][1:] not in m:
        m[ss[i][1:]]=0
    m[ss[i][1:]]|=1<<chi(ss[i][0])
ans=0
for i in range(n):
    s=""
    l=len(ss[i])
    for j in range(l,1,-1):
        if j!=l:
            s=ss[i][j]+s
        for k in range(26):
            if s in m:
                if (m[s]>>k)&1:
                    if (check[i][j-1]>>k)&1:
                        ans+=1
print(ans)