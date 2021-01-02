#pypyはinput使えない

import sys
n,q=map(int,sys.stdin.readline().split())
tree=[list(map(int,sys.stdin.readline().split())) for i in range(n-1)]
#f1は使ったのかどうかを表すフラッグ
#f2はそれまでに出てきたものを表すフラッグ
f1=[0]*(n-1)
f2=[0]*n
f2[0]=1

c=[0]*n
for i in range(q):
    p,x=map(int,sys.stdin.readline().split())
    c[p-1]+=x

while f1!=[1]*(n-1):
    for i,t in enumerate(tree):
        if f1[i]==0:
            if f2[t[0]-1]==1:
                c[t[1]-1]+=c[t[0]-1]
                f1[i]=1
                f2[t[1]-1]=1
            elif f2[t[1]-1]==1:
                c[t[0]-1]+=c[t[1]-1]
                f1[i]=1
                f2[t[0]-1]=1
            else:
                pass

print(" ".join([str(k) for k in c]))
