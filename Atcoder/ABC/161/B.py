n,m=map(int,input().split())
b=list(map(int,input().split()))
s=sum(b)
a=[i for i in b if i>=s/(4*m)]
print("Yes" if len(a)>=m else "No")