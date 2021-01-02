#xが何秒か分からないととりあえず何もできなそう
#xの個数数えてとかやりたいけどあまりにも面倒
#xは1から高々T秒、ならば二分探索でいける
#普通のdfs(上下左右)とかで記録していって、考えれば良さそう
#実装つら、dfsの練習になった
#多分OK

h,w,T=map(int,input().split())

st=[[0]*w for i in range(h)]

s=[0,0]
g=[0,0]
for i in range(h):
    x=input()
    for j in range(w):
        if x[j]=="#":
            st[i][j]=1
        elif x[j]=="S":
            st[i][j]=2
            s=[i,j]
        elif x[j]=="G":
            st[i][j]=3
            g=[i,j]

d=[[1000000000000000000]*w for i in range(h)]

def change(t,now,i,j):
    global st,d
    if st[i][j]==0:
        if d[i][j]>now+1:
            d[i][j]=now+1
            dfs(t,now+1,i,j)
    elif st[i][j]==1:
        if d[i][j]>now+t:
            d[i][j]=now+t
            dfs(t,now+t,i,j)
    elif st[i][j]==3:
        if d[i][j]>now+1:
            d[i][j]=now+1

#dfsはこんな感じで書くと書きやすい
def dfs(t,now,i,j):#初めはスタートの座標
    global st,d
    if i>0:change(t,now,i-1,j)
    if j>0:change(t,now,i,j-1)
    if i<h-1:change(t,now,i+1,j)
    if j<w-1:change(t,now,i,j+1)

def check(t):
    global s,g,d
    d=[[1000000000000000000]*w for i in range(h)]
    dfs(t,0,s[0],s[1])
    return d[g[0]][g[1]]

l,r=1,T
while l+1<r:
    k=(l+r)//2
    if check(k)<=T:
        l=k
    else:
        r=k
if check(r)<=T:
    print(r)
else:
    print(l)
