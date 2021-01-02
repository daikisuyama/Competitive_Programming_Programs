w,h=map(int,input().split())
w-=1
h-=1
ans=1
mod=10**9+7
for i in range(w+1,w+h+1):
    ans*=i
for i in range(1,h+1):
    ans//=i
print(ans%mod)