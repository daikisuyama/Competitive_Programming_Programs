import itertools
import math

n=int(input())
x=[list(map(int,input().split())) for i in range(n)]
y=list(itertools.permutations(x))


def dist(g):
    global n
    c=0
    for i in range(n-1):
        c+=math.sqrt((g[i+1][0]-g[i][0])**2+(g[i+1][1]-g[i][1])**2)
    return c

m=0
k=0
for i in y:
    k+=1
    m+=dist(i)
print(m/k)
