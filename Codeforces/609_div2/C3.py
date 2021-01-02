n,k=map(int,input().split())
a=list(map(int,input()))
ans=[-1]*n
upper=False
lower=False
for i in range(k):
    ans[i]=a[i]
for i in range(k,n):
    ans[i]=ans[i-k]
    if ans[i]==a[i]:
        pass
    elif ans[i]>a[i]:
        if lower==False and upper==False:
            upper=True
    else:
        if lower==False and upper==False:
            lower=True
            for j in range(k-1,-1,-1):
                if ans[j]!=9:
                    break
            for l in range(i+1):
                if l%k==j:
                    ans[l]+=1
                elif l%k>j:
                    ans[l]=0

print(n)
print("".join(map(str,ans)))