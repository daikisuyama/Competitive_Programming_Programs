for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    a.sort()
    ans=[]
    for i in range(n//2):
        ans.append(a[i])
        ans.append(a[n-1-i])
    if n%2==1:
        ans.append(a[n//2])
    print(" ".join(map(str,ans[::-1])))