import math

def distance_points1(i,j):
    global txa,tya
    return math.sqrt((txa-i)**2+(tya-j)**2)

def distance_points2(i,j):
    global txb,tyb
    return math.sqrt((txb-i)**2+(tyb-j)**2)


txa,tya,txb,tyb,T,V=map(int,input().split())
a=[txa,tya]
b=[txb,tyb]
D=T*V
n=int(input())
xy=[list(map(int,input().split())) for i in range(n)]

for i in range(n):
    d=distance_points1(xy[i][0],xy[i][1])+distance_points2(xy[i][0],xy[i][1])
    if d<=D:
        print("YES")
        break
else:
    print("NO")
