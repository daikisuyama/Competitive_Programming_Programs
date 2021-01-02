n,k=map(int,input().split())
x=[0]*(10**5)#1~10**5
for i in range(n):
    a,b=map(int,input().split())
    x[a-1]+=b
for i in range(10**5):
    k-=x[i]
    if k<=0:
        print(i+1)
        break
