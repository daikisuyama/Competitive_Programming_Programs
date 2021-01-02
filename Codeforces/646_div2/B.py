for _ in range(int(input())):
    s=input()
    n=len(s)
    c0,c1=s.count("1"),s.count("1")
    ans=min(c0,c1)
    #0...0の場合の左から変化
    for i in range(n):
        if s[i]=="0":
            c0+=1
        else:
            c0-=1
        ans=min(ans,c0)
    #右から
    for i in range(n-1,-1,-1):
        if s[i]=="0":
            c1+=1
        else:
            c1-=1
        ans=min(ans,c1)
    print(ans)