from collections import deque
def bfs():
    global n,m,s,d,check
    #print(d)
    while len(d):
        l=len(d)
        for i in range(l):
            p=d.popleft()
            for j in [[p[0],p[1]+1],[p[0],p[1]-1],[p[0]+1,p[1]],[p[0]-1,p[1]]]:
                #print([[p[0],p[1]+1],[p[0],p[1]-1],[p[0]+1,p[1]],[p[0]-1,p[1]]])
                #print(check[j[0]][j[1]])
                if not check[j[0]][j[1]]:
                    check[j[0]][j[1]]=True
                    d.append(j)
        #print(d)

for _ in range(int(input())):
    n,m=map(int,input().split())
    s=[["#" for i in range(m+2)]]+[list("#"+input()+"#") for i in range(n)]+[["#" for i in range(m+2)]]
    f=False
    #Bの周りを埋める
    for i in range(1,n+1):
        for j in range(1,m+1):
            if s[i][j]=="B":
                for k in [[i,j+1],[i,j-1],[i-1,j],[i+1,j]]:
                    if s[k[0]][k[1]]=="G":
                        f=True
                    elif s[k[0]][k[1]]==".":
                        s[k[0]][k[1]]="#"
    #print(s)
    if f:
        print("No")
        continue
    #bfsで探索
    if s[n][m]=="B" or s[n][m]=="#":
        for i in range(1,n+1):
            for j in range(1,m+1):
                if s[i][j]=="G":
                    f=True
        if not f:
            print("Yes")
        else:
            print("No")
        continue
    d=deque()
    d.append([n,m])
    check=[[(s[i][j]=="B") or (s[i][j]=="#") for j in range(m+2)] for i in range(n+2)]
    check[n][m]=True
    #print(check)
    bfs()
    for i in range(1,n+1):
        for j in range(1,m+1):
            if s[i][j]=="G" and check[i][j]==False:
                f=True
    #if f:
        #print(s)
        #print(check)
    #print(3)
    if f:
        print("No")
        continue
    print("Yes")
