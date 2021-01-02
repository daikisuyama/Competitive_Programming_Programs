n,k=map(int,input().split())
if k>(n-1)*n//2-(n-1):
    print(-1)
else:
    ans=[(1,i) for i in range(2,n+1)]
    lestnum=(n-1)*n//2-(n-1)-k
    for i in range(2,n):
        for j in range(i+1,n+1):
            if lestnum!=0:
                ans.append((i,j))
                lestnum-=1
    print(len(ans))
    for i in ans:
        print(" ".join(map(str,i)))