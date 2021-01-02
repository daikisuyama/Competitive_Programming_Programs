#フィボナッチ数列か…
#c問題も解けないのか…
#典型問題なんだろうな
#踏めない段の分は除いて考えれば良い
n,m=input().split()
n,m=int(n),int(m)
#壊れているのを0、いないのを1
ax=[1]*(n+1)
for i in range(m):
    ax[int(input())]=0
#前から順に加えてく
#壊れているばあいは0
bx=[1,1]
for i in range(2,n+1):
    if ax[i-1]==1:
        f1=bx[i-1]
    else:
        f1=0
    if ax[i-2]==1:
        f2=bx[i-2]
    else:
        f2=0
    bx.append((f1+f2)%(10**9+7))

print(bx[n])
