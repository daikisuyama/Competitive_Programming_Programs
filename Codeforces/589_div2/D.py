import sys
input=sys.stdin.readline
n,m=map(int,input().split())
tree=[set() for i in range(n)]
for i in range(m):
    a,b=map(int,input().split())
    tree[a-1].add(b-1)
    tree[b-1].add(a-1)
#print(tree)
check=[-1]*n
seen=[False]*n
now=1
for i in range(n):
    if not seen[i]:
        for j in range(n):
            if j not in tree[i]:
                check[j]=now
                seen[j]=True
                #print(i,j)
        now+=1
        if now==5:
            print(-1)
            exit()
if now==1 or now==2 or now==3:
    print(-1)
    exit()
#print(check)
setnum=[set() for i in range(n)]
s=[0]*n
for i in range(n):
    setnum[check[i]-1].add(i)
    s[check[i]-1]+=1
for i in range(n):
    if len(tree[i])+s[check[i]-1]!=n:
        print(-1)
        exit()
    for j in tree[i]:
        if j in setnum[check[i]-1]:
            print(-1)
            exit()
print(" ".join(map(str,check)))
