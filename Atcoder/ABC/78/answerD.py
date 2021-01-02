#難しく考えすぎていた
#こういう問題は最後どうなるかを考える
#最後は結局一番最後のカードを必ず引くことになる
#そのカードをどちらが引くのか
#先攻が圧倒的有利

n,z,w=map(int,input().split())
a=list(map(int,input().split()))

now=0
turn=True#xのターン
x,y=z,w
while now<n-1:
    print(now)
    if turn:
        far=[now,a[now]]
        for i in range(now,n):
            if abs(far[1]-y)<=abs(a[i]-y):
                far[0]=i
                far[1]=a[i]
        now=far[0]+1
        turn=not turn
        x=far[1]
    else:
        near=[now,a[now]]
        for i in range(now,n):
            if abs(near[1]-x)>abs(a[i]-x):
                near[0]=i
                near[1]=a[i]
        now=near[0]+1
        turn=not turn
        y=near[1]
if now==n-1:
    if turn:
        print(abs(a[-1]-y))
    else:
        print(abs(a[-1]-x))
else:
    print(abs(x-y))

print(x)
print(y)



