a,b,c=map(int,input().split())
k=int(input())
ans=0
while a>=b:
    ans+=1
    b*=2
while b>=c:
    ans+=1
    c*=2
print("Yes" if ans<=k else "No")