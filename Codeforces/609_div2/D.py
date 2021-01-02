n=int(input())
a=list(map(int,input().split()))
#わかんねえ
#ドミノを敷き詰める系→市松模様に塗る(は？)
w,b=0,0
for i in range(n):
    if i%2==0:
        w+=a[i]//2
        b+=a[i]-a[i]//2
    else:
        b+=a[i]//2
        w+=a[i]-a[i]//2
print(min(b,w))