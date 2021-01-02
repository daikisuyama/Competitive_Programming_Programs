import sys
sys.setrecursionlimit(10**6)
n,A,B,C=map(int,input().split())
s=[input() for i in range(n)]
def dfs(d,a,b,c,now):
    global n,s
    if d==n:
        print("Yes")
        for i in range(n):
            print(now[i])
        sys.exit()
    else:
        if s[d][0]=="A" and s[d][1]=="B":
            if a>b:
                dfs(d+1,a-1,b+1,c,now+"B")
            elif a<b:
                dfs(d+1,a+1,b-1,c,now+"A")
            else:
                if a>0:
                    dfs(d+1,a-1,b+1,c,now+"B")
                if b>0:
                    dfs(d+1,a+1,b-1,c,now+"A")
        elif s[d][0]=="A" and s[d][1]=="C":
            if a>c:
                dfs(d+1,a-1,b,c+1,now+"C")
            elif a<c:
                dfs(d+1,a+1,b,c-1,now+"A")
            else:
                if a>0:
                    dfs(d+1,a-1,b,c+1,now+"C")
                if c>0:
                    dfs(d+1,a+1,b,c-1,now+"A")
        else:
            if b>c:
                dfs(d+1,a,b-1,c+1,now+"C")
            elif b<c:
                dfs(d+1,a,b+1,c-1,now+"B")
            else:
                if b>0:
                    dfs(d+1,a,b-1,c+1,now+"C")
                if c>0:
                    dfs(d+1,a,b+1,c-1,now+"B")

dfs(0,A,B,C,"")
print("No")