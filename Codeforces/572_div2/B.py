n=int(input())
a=list(map(int,input().split()))
a.sort(reverse=True)
a1,a2=[a[i] for i in range(n) if i%2==0],[a[i] for i in range(n) if i%2==1]
b=a1+a2[::-1]
for i in range(n-1):
    if b[i]>=b[i-1]+b[i+1]:
        print("NO")
        break
else:
    if b[n-1]>=b[0]+b[n-2]:
        print("NO")
    else:
        print("YES")
        print(" ".join(map(str,b)))