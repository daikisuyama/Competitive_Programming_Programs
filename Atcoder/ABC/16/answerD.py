import numpy as np

def crossing_judge(p1,p2,p3,p4):
    t1 = (p1[0] - p2[0]) * (p3[1] - p1[1]) + (p1[1] - p2[1]) * (p1[0] - p3[0])
    t2 = (p1[0] - p2[0]) * (p4[1] - p1[1]) + (p1[1] - p2[1]) * (p1[0] - p4[0])
    t3 = (p3[0] - p4[0]) * (p1[1] - p3[1]) + (p3[1] - p4[1]) * (p3[0] - p1[0])
    t4 = (p3[0] - p4[0]) * (p2[1] - p3[1]) + (p3[1] - p4[1]) * (p3[0] - p2[0])
    return t1*t2<0 and t3*t4<0

ax,ay,bx,by=map(int,input().split())
a=np.array([ax,ay])
b=np.array([bx,by])
n=int(input())
xy=[np.array(list(map(int,input().split()))) for i in range(n)]
cnt=0
for i in range(n-1):
    cnt+=crossing_judge(a,b,xy[i],xy[i+1])
cnt+=crossing_judge(a,b,xy[n-1],xy[0])
print(cnt//2+1)