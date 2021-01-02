n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
de=10**12
for i in range(n-1,-1,-1):
    if a[i]>=de:
        continue
    if b[i]<a[i]:
        de=a[i]-b[i]
    else:
        print(b[i]-a[i]+1)
        exit()
print(0)