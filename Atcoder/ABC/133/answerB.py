import math
#numpy使った方がよかったか
N,D=input().split()
N,D=int(N),int(D)
X=[]

for i in range(N):
    X1=input().split()
    #print(X[i])
    X2=[]
    for j in range(D):
        X2.append(int(X1[j]))
    X.append(X2)
    
c=0
for i in range(N):
    for j in range(N-i-1):
        d=0
        for k in range(D):
            d+=(X[i][k]-X[j+i+1][k])**2
        if abs(math.sqrt(d)-int(math.sqrt(d))) <0.0001:
            c+=1

print(c)
