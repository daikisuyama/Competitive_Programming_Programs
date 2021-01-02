n=int(input())
k=int(input())
x=[int(i) for i in input().split()]
cnt=0
for i in range(n):
    cnt+=min(abs(k-x[i]),x[i])
print(2*cnt)
