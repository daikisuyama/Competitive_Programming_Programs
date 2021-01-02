N,X=input().split()
N,X=int(N),int(X)

L1=input().split()
L2=[]
for i in L1:
    L2.append(int(i))

c=1
d=0
for i in range(N):
    d+=L2[i]
    if d<=X:
        c+=1
    else:
        break

print(c)
