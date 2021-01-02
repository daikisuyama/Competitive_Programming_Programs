n,*p=map(int,open(0).read().split())
for i in range(1,n):p[i]=min(p[~-i],p[i])
print(len(set(p)))
