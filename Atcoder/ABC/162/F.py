n=int(input())
a=list(map(int,input().split()))
ans=[]
if n%2==0:
    ans1,ans2=0,0
    for i in range(n):
        if i%2==0:
            ans1+=a[i]
        else:
            ans2+=a[i]
    print(max(ans1,ans2))
else:
    a1,a2=[],[]
    for i in range(n):
        if i%2==0:
            a1.append(a[i])
        else:
            a2.append(a[i])
        ans1,ans2,ans3=0,0,0
    for i in range(n-1):
        if i%2==0:
            ans1+=a[i]
        else:
            ans2+=a[i]
    print(max([ans1,ans2,ans1-a[0]+a[-1]]))