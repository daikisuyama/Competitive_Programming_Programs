for _ in range(int(input())):
    a,b,c=map(int,input().split())
    ans=[]
    if a<c:
        ans.append(1)
    else:
        ans.append(-1)
    if a*b>c:
        ans.append(b)
    else:
        ans.append(-1)
    print(" ".join(map(str,ans)))