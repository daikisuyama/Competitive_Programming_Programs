a,b,c,k=map(int,input().split())
s,t=map(int,input().split())

ans=a*s+b*t
if s+t>=k:
    print(ans-c*(s+t))
else:
    print(ans)
