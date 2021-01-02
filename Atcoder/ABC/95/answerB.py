n,x=map(int,input().split())
m=[int(input()) for i in range(n)]
m.sort()
x-=sum(m)
ans=n
print(ans+x//m[0])