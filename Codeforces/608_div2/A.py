a,b,c,d,e,f=[int(input()) for i in range(6)]
if e<f:
    m=min(b,c,d)
    ans=m*f
    b-=m
    c-=m
    d-=m
    ans+=min(a,d)*e
else:
    m=min(a,d)
    ans=m*e
    a-=m
    d-=m
    ans+=min(b,c,d)*f
print(ans)
