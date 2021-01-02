import fractions
a,b,c=map(int,input().split())
d=fractions.gcd(a,b)

if c%d==0:
    print("YES")
else:
    print("NO")
