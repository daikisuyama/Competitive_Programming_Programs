a,b,c=map(int,input().split())
p=(a%2!=b%2)or(b%2!=c%2)
a,b,c=sorted([a+((a%2==b%2)^(a%2==c%2)),b+((b%2==a%2)^(b%2==c%2)),c+((c%2==a%2)^(c%2==b%2))])
print((c-a)//2+(c-b)//2+p)