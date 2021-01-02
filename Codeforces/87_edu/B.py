t=int(input())
for i in range(t):
    s=input()
    le=len(s)
    l,r=0,0
    d=[0,0,0]
    d[int(s[0])-1]=1
    ans=0
    while True:
        #rの決定
        while not all(d) and r!=le-1:
            r+=1
            d[int(s[r])-1]+=1
            if r==le-1:
                break
        #lの決定
        while l!=le-1:
            if all(d):
                if ans==0:
                    ans=r-l+1
                else:
                    ans=min(ans,r-l+1)
                d[int(s[l])-1]-=1
                l+=1
            else:
                break
        if r==le-1 or l==le-1:
            break
    print(ans)

