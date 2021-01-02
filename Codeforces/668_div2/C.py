for _ in range(int(input())):
    n,k=map(int,input().split())
    s=input()
    t=[[] for i in range(k)]
    for i in range(n):
        t[i%k].append(s[i])
    #違うものあったらその時点でだめ
    ans0,ans1=0,0
    ex=0
    for i in range(k):
        if t[i].count("0")>0 and t[i].count("1")>0:
            print("NO")
            break
        elif t[i].count("0")>0:
            ans0+=1
        elif t[i].count("1")>0:
            ans1+=1
        else:
            ex+=1
    else:
        if ex==0:
            if ans0==ans1:
                print("YES")
            else:
                print("NO")
        else:
            if ans0+ex>=k//2 and ans1+ex>=k//2:
                print("YES")
            else:
                print("NO")
