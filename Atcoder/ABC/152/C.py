n=int(input())
p=[int(i) for i in input().split()]
mi=10000000
x=[0]*n
for i in range(n):
    if mi>p[i]:
        x[i]=1
        mi=p[i]
print(sum(x))
