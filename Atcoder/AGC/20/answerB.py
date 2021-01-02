n=int(input())
a=list(map(int,input().split()))
if a[n-1]!=2:
    print(-1)
    exit()
check=[0]*n
check[n-1]=2
#ここの条件が怪しいか
#問題文をもう一回読む
for i in range(n-2,-1,-1):
    check[i]=(-(-check[i+1]//a[i])*a[i])
check2=[0]*n
check2[n-1]=2
#ここ詰められなくて30分くらい
#わからんかった
#は？わかんねええええええ
#なんで何
for i in range(n-2,-1,-1):
    check2[i]=(check2[i+1]+a[i+1]-1)//a[i]*a[i]
ex=[check[0],check2[0]+a[0]-1]
for i in range(n):
    ex[0]=(ex[0]//a[i])*a[i]
    ex[1]=(ex[1]//a[i])*a[i]
if ex==[2,2]:
    print(check[0],check2[0]+a[0]-1)
else:
    print(-1)