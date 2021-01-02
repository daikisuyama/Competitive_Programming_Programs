n=int(input())
k=int(input())
x=1
for i in range(n):
    x=min(x+k,2*x)
print(x)