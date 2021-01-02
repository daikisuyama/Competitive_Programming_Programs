x=input().split()
k,X=int(x[0]),int(x[1])
a=X-k+1
b=X+k-1
for i in range(2*k-1):
    print(a+i,end=" ")
print()
