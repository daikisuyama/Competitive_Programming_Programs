x=[0]*9
n=int(input())
a=[int(i) for i in input().split()]
for i in range(n):
    for j in range(8):
        if a[i]<400*(j+1):
            x[j]=1
            break
    else:
        x[8]+=1

if x[:-1].count(1)!=0:
    print(x[:-1].count(1),end=" ")
else:
    print(1,end=" ")
print(x[:-1].count(1)+x[-1])
