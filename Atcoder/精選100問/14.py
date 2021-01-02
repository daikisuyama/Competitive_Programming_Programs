#11/26 10:33~10:40,+1分
#あれ、WA(場合分けミス)
n,k=map(int,input().split())
a=list(map(int,input().split()))
ans=10**30
for i in range(2**n):
    if sum((i>>j)&1 for j in range(n))<k:continue
    ans_sub=0
    m=a[0]
    for j in range(1,n):
        if (i>>j)&1:
            if m>=a[j]:
                ans_sub+=((m+1)-a[j])
                m+=1
            else:
                m=max(m,a[j])
        else:
            m=max(m,a[j])
    ans=min(ans,ans_sub)
print(ans)