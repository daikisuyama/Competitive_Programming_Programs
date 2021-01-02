for _ in range(int(input())):
    n=int(input())
    s=[i=="A" for i in list(input())]
    tim=[s]
    ans=0
    while True:
        t=[s[0]]
        for i in range(n-1):
            if tim[-1][i]==1:
                t.append(True)
            else:
                t.append(tim[-1][i+1])
        #print(s,t)
        if tim[-1]==t:
            break
        ans+=1
        tim.append(t)
        #print(s,t)
    print(ans)