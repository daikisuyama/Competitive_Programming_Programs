n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
s=sum(a)
e,o=[b[i]-a[i] for i in range(n) if i%2==0],[b[i]-a[i] for i in range(n) if i%2==1]
e.sort(reverse=True)
o.sort(reverse=True)
for i in range(n//2):
    if e[i]+o[i]>0:
        s+=e[i]+o[i]
    else:
        break
print(s)