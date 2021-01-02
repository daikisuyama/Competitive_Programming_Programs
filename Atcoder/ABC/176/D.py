#辺の重み(変化量)が0である場合は01DFSって特別なやつ
#0の場合はそこでBFSできる
import sys
from collections import deque
sys.setrecursionlimit(10**7)
input=sys.stdin.readline
h,w=map(int,input().split())
c=[int(i)-1 for i in input().split()]
d=[int(i)-1 for i in input().split()]
s=[input() for i in range(h)]
inf=100000000
dp=[[-1 if s[i][j]=="#" else inf for j in range(w)] for i in range(h)]
dp[c[0]][c[1]]=0
now=deque([[c[0],c[1]]])
#グリッド上のbfsはfor文で
def bfs():
    global h,w,s,dp,now
    while len(now):
        i,j=now.popleft()
        for k,l in [[i-1,j],[i+1,j],[i,j-1],[i,j+1]]:
            if 0<=k<h and 0<=l<w:
                if dp[k][l]!=-1:
                    if dp[k][l]>dp[i][j]:
                        dp[k][l]=dp[i][j]
                        now.appendleft([k,l])
        for k in range(i-2,i+3):
            for l in range(j-2,j+3):
                if 0<=k<h and 0<=l<w:
                    if dp[k][l]!=-1:
                        if dp[k][l]>dp[i][j]+1:
                            dp[k][l]=dp[i][j]+1
                            now.append([k,l])
bfs()
print(dp[d[0]][d[1]] if dp[d[0]][d[1]]!=inf else -1)