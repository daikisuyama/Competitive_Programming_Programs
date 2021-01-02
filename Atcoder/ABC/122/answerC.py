n,q=map(int,input().split())
s=input()
x=[0]*n

for i in range(n-1):
    if s[i:i+2]=="AC":
        x[i+1]=x[i]+1
    else:
        x[i+1]=x[i]
for i in range(q):
    l,r=map(int,input().split())
    print(x[r-1]-x[l-1])
