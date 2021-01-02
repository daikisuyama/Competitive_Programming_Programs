n,m=input().split()
n,m=int(n),int(m)
#nは23まである
if n>=12:
    n-=12
a=6*m
b=30*n+0.5*m
#小さい方ならmin使えばいいやん
print(min([360-abs(a-b),abs(a-b)]))
