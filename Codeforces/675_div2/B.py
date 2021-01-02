for _ in range(int(input())):
    n,m=map(int,input().split())
    mat=[list(map(int,input().split())) for i in range(n)]
    check=[[0]*m for i in range(n)]
    segments=[]
    for i in range(n):
        for j in range(m):
            if check[i][j]==0:
                seg_sub=[]
                check[i][j]=1
                seg_sub.append(mat[i][j])
                if n%2==0 or i!=n//2:
                    check[n-1-i][j]=1
                    seg_sub.append(mat[n-1-i][j])
                    if m%2==0 or j!=m//2:
                        check[i][m-1-j]=1
                        check[n-1-i][m-1-j]=1
                        seg_sub.append(mat[i][m-1-j])
                        seg_sub.append(mat[n-1-i][m-1-j])
                else:
                    if m%2==0 or j!=m//2:
                        check[i][m-1-j]=1
                        seg_sub.append(mat[i][m-1-j])
                segments.append(seg_sub)
    ans=0
    for i in segments:
        seg=sorted(i)
        m=len(seg)//2
        for i in seg:
            ans+=abs(i-seg[m])
    print(ans)