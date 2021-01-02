a,b,c,x=int(input()),int(input()),int(input()),int(input())
x//=50
ans=0
for i in range(x//10+1):
    k=x-i*10
    for j in range(k//2+1):
        l=k-j*2
        ans+=(0<=i<=a and 0<=j<=b and 0<=l<=c)
print(ans)