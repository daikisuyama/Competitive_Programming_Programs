for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    xy=[[] for i in range(2)]
    for i in range(2*n):
        xy[a[i]%2].append(i+1)
    ans=[]
    for i in range(2):
        for j in range(len(xy[i])//2):
            ans.append([xy[i][2*j],xy[i][2*j+1]])
    for i in range(n-1):
        print(" ".join(map(str,ans[i])))