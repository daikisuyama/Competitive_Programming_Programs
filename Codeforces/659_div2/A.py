for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    s="a"*50
    ans=[s]
    for i in range(n):
        s=""
        for j in range(50):
            if j<a[i]:
                s+=ans[-1][j]
            else:
                if ans[-1][j]=="a":
                    s+="b"
                else:
                    s+="a"
        ans.append(s)
    for i in range(n+1):
        print(ans[i])