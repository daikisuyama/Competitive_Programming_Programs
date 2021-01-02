n=int(input())
a=list(map(int,input().split()))
#ギャグ
mod=10**9+7
if min(a)==0:
    print(-1)
    exit()
if max(a)>3:
    print(mod)
    exit()
ans=1
for i in a:
    sub=1
    for j in range(i):
        sub*=(j+1)
    ans*=(i**sub)
    if ans>10**9+7:
        print(mod)
        exit()
print(mod%ans)