#誤読…
t=int(input())
for _ in range(t):
    n,a,b=int(input()),input(),input()
    ans=[]
    for i in range(n):
        if a[i]!=b[i]:
            ans.append(f"{i+1}")
            ans.append("1")
            ans.append(f"{i+1}")
    print(f"{len(ans)}"+" "+" ".join(ans))