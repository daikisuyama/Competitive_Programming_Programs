from collections import deque
ans=0
n,m=map(int,input().split())
x=[input() for i in range(n)]
for i in [chr(i) for i in range(97, 97+26)]:
    y=[[int(x[k][j]==i)  for j in range(m)] for k in range(n)]
    check=[[x[k][j]!=i  for j in range(m)] for k in range(n)]
    #四方向が同じでなければ続ける
    d=2
    b=deque()
    for j in range(n):
        for k in range(m):
            if j==0 or j==n-1 or k==0 or k==m-1:
                if y[j][k]:
                    check[j][k]=True
                    b.append([j,k])
            elif not (y[j-1][k] and y[j+1][k] and y[j][k-1] and y[j][k+1]):
                if y[j][k]:
                    check[j][k]=True
                    b.append([j,k])
    while len(b):
        l=len(b)
        for _ in range(l):
            c=b.popleft()
            if c[0]>0:
                if not check[c[0]-1][c[1]]:
                    check[c[0]-1][c[1]]=True
                    y[c[0]-1][c[1]]=d
                    b.append([c[0]-1,c[1]])
            if c[0]<n-1:
                if not check[c[0]+1][c[1]]:
                    check[c[0]+1][c[1]]=True
                    y[c[0]+1][c[1]]=d
                    b.append([c[0]+1,c[1]])
            if c[1]>0:
                if not check[c[0]][c[1]-1]:
                    check[c[0]][c[1]-1]=True
                    y[c[0]][c[1]-1]=d
                    b.append([c[0],c[1]-1])
            if c[1]<m-1:
                if not check[c[0]][c[1]+1]:
                    check[c[0]][c[1]+1]=True
                    y[c[0]][c[1]+1]=d
                    b.append([c[0],c[1]+1])
        d+=1
    #print(y)
    #ans2=ans
    for j in range(n):
        for k in range(m):
            ans+=y[j][k]
    #print(ans-ans2)
print(ans)