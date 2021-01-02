from math import gcd
n=int(input())
points=[list(map(int,input().split())) for i in range(n)]
def calc(i,j,k):
    global points,n
    vec1=[points[i][0]-points[j][0],points[i][1]-points[j][1]]
    vec2=[points[i][0]-points[k][0],points[i][1]-points[k][1]]
    return vec1[0]*vec2[1]==vec1[1]*vec2[0]
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            if calc(i,j,k):
                print("Yes")
                exit()
print("No")