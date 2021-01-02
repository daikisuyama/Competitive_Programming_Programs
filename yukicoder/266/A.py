n=int(input())
ans=0
for i in range(n//5+1):
    for j in range(n//2+1):
        for k in range(n//3+1):
            ans+=(i*5+j*2+k*3==n and i>=j)
print(ans)