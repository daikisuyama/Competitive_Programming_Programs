import itertools
n,m=map(int,input().split())
p=[[0]*n for i in range(n)]#隣接行列
for i in range(m):
    a,b=map(int,input().split())
    p[a-1][b-1]=1
    p[b-1][a-1]=1
seq=(i for i in range(n))
x=list(itertools.permutations(seq))
#print(x[0])
l=len(x)
ans=0
for i in range(l):
    k=x[i]
    if k[0]==0:
        for j in range(n-1):
            if p[k[j]][k[j+1]]!=1:
                break
        else:
            ans+=1
            #print(k)
    else:
        break
print(ans)
