for _ in range(int(input())):
    n=int(input())
    ans=[]
    ai=1
    n-=1
    xi=0
    while True:
        if n<=2*ai:
            xi=n-ai
            ai=ai+xi
            n-=ai
            ans.append(xi)
            break
        elif n<=3*ai:
            xi=0
            ai=ai+xi
            n-=ai
            ans.append(xi)
        elif n<4*ai:
            xi=ai//2
            ai=ai+xi
            n-=ai
            ans.append(xi)
        else:
            xi=ai
            ai=ai+xi
            n-=ai
            ans.append(xi)
            #print(2)
        #print(ai,xi,n)
    print(len(ans))
    print(" ".join(map(str,ans)))