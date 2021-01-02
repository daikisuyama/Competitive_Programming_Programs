n,k=map(int,input().split())
p=list(map(int,input().split()))
ans=[sum([(p[i]+1)/2 for i in range(k)])]
for i in range(n-k):
    ans.append(ans[-1]-(p[i]+1)/2+(p[k+i]+1)/2)
print(max(ans))