#PyPy遅え
import sys
sys.setrecursionlimit(400000000)
inf=1000000000000000000
n,m=map(int,input().split())
x=[inf]*n
#まだ訪問してなければTrue
check=[True]*n
#どこと関係があるかを記録する(maybe right)
lrd=[[] for i in range(n)]
for i in range(m):
    l,r,d=map(int,input().split())
    l-=1
    r-=1
    lrd[l].append((r,d))
    lrd[r].append((l,-d))
#wrong thought
#どっちも決まってない場合の処理
#決まってるとこからやれば良い
#ソートして順番に決めておく

#記録した関係から辿っていく
#まず初めのやつ決定
#非連結な場合を忘れていた


def bfs(z):
    #globalくらいちゃんとしろ
    global lrd,check,x
    for i in range(len(lrd[z])):
        k=lrd[z][i]
        if check[k[0]]:
            x[k[0]]=x[z]+k[1]
            check[k[0]]=False
            bfs(k[0])
        else:
            if x[k[0]]!=x[z]+k[1]:
                print("No")
                sys.exit()
st=0
while any(check):
    for i in range(st,n):
        if len(lrd[i])!=0 and check[i]:
            st=i
            break
        else:
            check[i]=False
    else:
        break
    x[st]=0
    check[st]=False
    bfs(st)
print("Yes")