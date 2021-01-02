#6で割ったときに、1,3,のパターン

n=int(input())
a=[int(i)%6 for i in input().split()]
c=0
for i in range(n):
    if a[i]>=3:
        c+=(a[i]-3)
    elif a[i]>=1:
        c+=(a[i]-1)
    else:
        c+=3
print(c)
