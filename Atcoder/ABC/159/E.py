h,w,k=map(int,input().split())
s=[[int(j) for j in input()] for i in range(h)]
def popcount(x):
    global h
    ret=0
    for i in range(h-1):
        ret+=(x>>i&1)
    return ret
#できない場合は除く
ans=1000000000000000
for i in range(2**(h-1)):
    p=popcount(i)
    div=[0]*(p+1)
    ans_sub=p
    f=False
    for j in range(w):
        now=0
        div[now]+=s[0][j]
        for l in range(h-1):
            if i>>l&1:
                now+=1
            div[now]+=s[l+1][j]
        if all(i<=k for i in div):
            continue
        else:
            div=[0]*(p+1)
            now=0
            div[now]=s[0][j]
            for l in range(h-1):
                if i>>l&1:
                    now+=1
                div[now]+=s[l+1][j]
            ans_sub+=1
            f=any(i>k for i in div)
    if not f:ans=min(ans,ans_sub)
print(ans)