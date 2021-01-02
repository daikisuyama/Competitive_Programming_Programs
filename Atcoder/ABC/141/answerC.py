n,k,q=map(int,input().split())
a=[0]*n
for i in range(q):
    n2=int(input())-1
    a[n2]+=1
for i in range(n):
    if a[i]+k-q>0:
        print("Yes")
    else:
        print("No")
