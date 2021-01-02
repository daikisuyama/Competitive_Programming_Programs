import queue
r,c=map(int,input().split())
sy,sx=map(int,input().split())
gy,gx=map(int,input().split())

C=[list(input()) for i in range(r)]
Cm=[[-1]*c for i in range(r)]
s=[sy-1,sx-1]
g=[gy-1,gx-1]
q=queue.Queue()
q.put(s)
t=0
Cm[s[0]][s[1]]=t
#bfsの更新はたどり着く瞬間にやらないと無駄に計算量が増えてしまう
def bfs():
    global C,Cm,q,t
    while not q.empty():
        t+=1
        l=q.qsize()
        for k in range(l):
            i,j=q.get()
            if i-1>=0:
                if C[i-1][j]=="." and Cm[i-1][j]==-1:
                    q.put([i-1,j])
                    Cm[i-1][j]=t
            if j-1>=0:
                if C[i][j-1]=="." and Cm[i][j-1]==-1:
                    q.put([i,j-1])
                    Cm[i][j-1]=t
            if i+1<=r-1:
                if C[i+1][j]=="." and Cm[i+1][j]==-1:
                    q.put([i+1,j])
                    Cm[i+1][j]=t
            if j+1<=c-1:
                if C[i][j+1]=="." and Cm[i][j+1]==-1:
                    q.put([i,j+1])
                    Cm[i][j+1]=t
        if Cm[g[0]][g[1]]!=-1:
            print(Cm[g[0]][g[1]])
            break
bfs()
