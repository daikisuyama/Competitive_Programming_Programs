for _ in range(int(input())):
    n=int(input())
    s=[input() for i in range(n)]
    t=set(s)
    a,b,c,d=set(),set(),set(),set()
    for i in range(n):
        if s[i][0]=="0":
            if s[i][-1]=="0":
                c.add(i)
            else:
                a.add(i)
        else:
            if s[i][-1]=="0":
                b.add(i)
            else:
                d.add(i)
    l=set()
    for i in range(n):
        if (i in a or i in b) and (s[i][::-1] in t):
            l.add(i)
    la,lb,lc,ld,ll=len(a),len(b),len(c),len(d),len(l)
    #print(la,lb,lc,ld,ll)
    if la==0 and lb==0:
        if lc==0 or ld==0:
            print(0)
        else:
            print(-1)
        continue
    if lb>la:
        if lb-ll//2<(lb-la)//2*2:
            print(-1)
            continue
        x=(lb-la)//2
        print(x)
        if x==0:
            continue
        ans=[]
        for i in b:
            if i not in l:
                ans.append(str(i+1))
                x-=1
                if x==0:
                    break
        print(" ".join(ans))
    elif la>lb:
        if la-ll//2<(la-lb)//2*2:
            print(-1)
            continue
        x=(la-lb)//2
        print(x)
        if x==0:
            continue
        ans=[]
        for i in a:
            if i not in l:
                ans.append(str(i+1))
                x-=1
                if x==0:
                    break
        print(" ".join(ans))
    else:
        print(0)