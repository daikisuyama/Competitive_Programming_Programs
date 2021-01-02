n,a,b=map(int,input().split())

x=[int(i) for i in input().split()]

c=0
for i in range(n-1):
    c+=min((x[i+1]-x[i])*a,b)
print(c)
