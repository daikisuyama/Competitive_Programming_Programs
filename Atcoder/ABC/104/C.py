import math
d,g=map(int,input().split())
pc=[list(map(int,input().split())) for i in range(d)]
ans=10000000000000000000
for i in range(1<<d):
    s=0
    ans_=0
    for j in range(d):
        if (i>>j)&1:
            s+=(pc[j][1]+pc[j][0]*100*(j+1))
            ans_+=pc[j][0]
    if s>=g:
        ans=min(ans,ans_)
    else:
        for j in range(d-1,-1,-1):
            if not((i>>j)&1):
                if s+(pc[j][0]*100*(j+1))>=g:
                    h=-((s-g)//(100*(j+1)))
                    s+=(h*100*(j+1))
                    ans_+=h
                    ans=min(ans,ans_)
                    break
                else:
                    break
print(ans)
#ansとans_
#謎のWA