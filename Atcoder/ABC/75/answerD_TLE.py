import itertools
n,k=map(int,input().split())
xy=[list(map(int,input().split())) for i in range(n)]
t=[i for i in range(n)]
s=list(itertools.permutations(t,k))
#print(s)
l=len(s)
inf=10000000000
x_min=inf
y_min=inf
x_max=-inf
y_max=-inf
for i in range(n):
    x,y=xy[i]
    if x<x_min:x_min=x
    if y<y_min:y_min=y
    if x>x_max:x_max=x
    if y>y_max:y_max=y
area=(x_max-x_min)*(y_max-y_min)
for i in range(l):
    x_min=inf
    y_min=inf
    x_max=-inf
    y_max=-inf
    for j in range(k):
        x,y=xy[s[i][j]]
        if x<x_min:x_min=x
        if y<y_min:y_min=y
        if x>x_max:x_max=x
        if y>y_max:y_max=y
    #print(area)
    area=min((x_max-x_min)*(y_max-y_min),area)
print(area)