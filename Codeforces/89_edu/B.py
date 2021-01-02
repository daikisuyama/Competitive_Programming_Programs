for _ in range(int(input())):
    n,x,m=map(int,input().split())
    ans=[x,x]
    for i in range(m):
        l,r=map(int,input().split())
        if r<ans[0] or l>ans[1]:
            continue
        else:
            ans=[min(ans[0],l),max(ans[1],r)]
    print(ans[1]-ans[0]+1)