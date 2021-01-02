for _ in range(int(input())):
    n=int(input())
    ans=0
    for i in range(1,10):
        cand=[]
        while True:
            cand.append(str(i))
            x=int("".join(cand))
            if x<=n:
                ans+=1
            else:
                break
    print(ans)