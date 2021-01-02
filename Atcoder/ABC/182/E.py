from itertools import groupby
h,w,n,m=map(int,input().split())
check1=[[-1]*w for i in range(h)]
check2=[[-1]*h for i in range(w)]
for i in range(n):
    a,b=map(int,input().split())
    check1[a-1][b-1]=1
    check2[b-1][a-1]=1
for i in range(m):
    c,d=map(int,input().split())
    check1[c-1][d-1]=0
    check2[d-1][c-1]=0
#print(check1)
#print(check2)
for i in range(h):
    x=[(key,list(group)) for key,group in groupby(check1[i],key=lambda x:x==0)]
    now=0
    for k,g in x:
        if not k and 1 in g:
            for j in g:
                check1[i][now]=1
                now+=1
        else:
            now+=len(g)
for i in range(w):
    x=[(key,list(group)) for key,group in groupby(check2[i],key=lambda x:x==0)]
    now=0
    for k,g in x:
        if not k and 1 in g:
            for j in g:
                check2[i][now]=1
                now+=1
        else:
            now+=len(g)
ans=0
for i in range(h):
    for j in range(w):
        if check1[i][j]==1 or check2[j][i]==1:
            ans+=1
#print(check1)
#print(check2)
print(ans)