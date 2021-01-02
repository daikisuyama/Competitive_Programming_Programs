for _ in range(int(input())):
    p,f=map(int,input().split())
    cnts,cntw=map(int,input().split())
    s,w=map(int,input().split())
    if s>w:
        s,w=w,s
        cnts,cntw=cntw,cnts
    ans=0
    for i in range(cnts+1):
        if i*s>p:break
        ans_sub=0
        nows=cnts-i
        ans_sub+=i
        #sは選びずみ
        rest1=p-i*s
        #wの方
        noww=cntw-min(rest1//w,cntw)
        ans_sub+=min(rest1//w,cntw)
        #次のひと
        #sの方
        ans_sub+=min(f//s,nows)
        rest2=f-min(f//s,nows)*s
        #wの方
        ans_sub+=min(noww,rest2//w)
        ans=max(ans,ans_sub)
    print(ans)