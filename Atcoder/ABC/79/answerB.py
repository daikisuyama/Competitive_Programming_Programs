n=int(input())
k,l=2,1
for i in range(n-1):
    m=l
    l=k+l
    k=m
print(l)
