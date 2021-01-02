t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    s=input()
    dp=[set() for i in range(n+1)]
    dp[n]={0}
    for i in range(n,0,-1):
        if s[i-1]=="0":
            for j in dp[i]:
                dp[i-1].add(j)
                dp[i-1].add(j^a[i-1])
        else:
            if a[i-1] in dp[i]:
                for j in dp[i]:
                    dp[i-1].add(j)
            else:
                print(1)
                break
    else:
        print(0)