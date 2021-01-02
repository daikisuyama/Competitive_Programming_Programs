n,m=map(int,input().split())
if n%2==1:
    [print(i+1,n-i) for i in range(m)]
else:
    [print(i+1,n-i) if i<m/2 else print(i+1,n-i-1) for i in range(m)]