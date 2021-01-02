h,w,K=map(int,input().split())
c=[input() for i in range(h)]
ans=0
for i in range(2**h):
    for j in range(2**w):
        d=[[c[z][v] for v in range(w)]for z in range(h)]
        for k in range(h):
            if (i>>k)&1:
                for l in range(w):
                    d[k][l]="x"
        for k in range(w):
            if (j>>k)&1:
                for l in range(h):
                    d[l][k]="x"
        cnt=0
        for k in range(h):
            for l in range(w):
                cnt+=(d[k][l]=="#")
        ans+=(cnt==K)
print(ans)