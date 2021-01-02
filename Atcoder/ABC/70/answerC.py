import fractions
n=int(input())
t=[int(input()) for i in range(n)]

if n==1:
    print(t[0])
else:
    x=t[0]*t[1]//fractions.gcd(t[0],t[1])
    for i in range(1,n-1):
        x=x*t[i+1]//fractions.gcd(x,t[i+1])
    print(x)
