n,k=map(int,input().split())
s=[int(input()) for i in range(n)]

if 0 in s:
    print(n)
elif k==0:
    print(0)
elif n==1:
    if s[0]<=k:
        print(1)
    else:
        print(0)
else:
    #しゃくとり、どこからどこまで見てるか
    f1,f2=0,0
    t=s[0]
    ans=0
    for i in range(1,n):
        #print(ans)
        f2=i
        t*=s[i]
        if t>k:
            for j in range(f1,f2+1):
                t=t//s[j]
                if t<=k:
                    f1=j+1
                    ans=max(f2-f1+1,ans)
                    break
        else:
            ans=max(f2-f1+1,ans)
    print(ans)
