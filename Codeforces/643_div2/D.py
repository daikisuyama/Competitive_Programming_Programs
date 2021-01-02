n,s=map(int,input().split())
if n<s-(n-1):
    print("YES")
    print(" ".join(map(str,[1 if i!=n-1 else s-(n-1) for i in range(n)])))
    print(n)
else:
    print("NO")