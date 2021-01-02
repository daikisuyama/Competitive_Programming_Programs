from math import ceil
h,w,d=map(int,input().split())
x=ceil((h*w)/d)
num=[[[-1,-1] for j in range(x)] for i in range(d)]#あまりで場合分け(1→0)
mp=[[0]*x for i in range(d)]
a=[list(map(int,input().split())) for i in range(h)]
for i in range(h):
    for j in range(w):
        k,l=a[i][j]%d,a[i][j]//d
        if k==0:
            num[d-1][l-1]=[i,j]
        else:
            num[k-1][l]=[i,j]
for i in range(d):
    for j in range(x):
        if j!=x-1:
            if num[i][j+1]!=[-1,-1]:
                mp[i][j+1]+=(mp[i][j]+abs(num[i][j+1][0]-num[i][j][0])+abs(num[i][j+1][1]-num[i][j][1]))
            else:
                break
q=int(input())
for i in range(q):
    l,r=map(int,input().split())
    if l%d!=0:
        e,f=l//d,r//d
    else:
        e,f=l//d-1,r//d-1
    g= d-1 if l%d==0 else l%d-1
    if e==0:
        print(mp[g][f])
    else:
        print(mp[g][f]-mp[g][e])
