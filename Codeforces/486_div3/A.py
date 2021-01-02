n,k=map(int,input().split())
a=list(map(int,input().split()))
b=list(set(a))
if len(b)>=k:
    print("YES")
    ans=[]
    for i in range(k):
        ans.append(a.index(b[i])+1)
    print(" ".join(map(str,ans)))
else:
    print("NO")