n=int(input())
ans=0
for i in range(1,n+1):
    x,y=i,(n//i)*i
    ans+=((n//i)*(x+y)//2)
print(ans)