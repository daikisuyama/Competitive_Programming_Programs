a,b,c,d=map(int,input().split());x=range(c+d);D=[[0]*6011for _ in[0]*6011];D[a][b]=1
for i in x:
 for j in x:D[i+1][j+1]+=(D[i+1][j]*(i+1)+D[i][j+1]*(j+1)-D[i][j]*i*j)%998244353
print(D[c][d])