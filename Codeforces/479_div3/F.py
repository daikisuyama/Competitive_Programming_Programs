n=int(input())
a=list(map(int,input().split()))
s=dict()
for i in range(n):
    if a[i]-1 in s:
        s[a[i]]=s[a[i]-1]+1
    else:
        s[a[i]]=1
ans=[-1,-1]
for i in s:
    if ans[1]<s[i]:
        ans=[i,s[i]]
ans_=[]
for i in range(n-1,-1,-1):
    if ans[0]==a[i]:
        ans[0]-=1
        ans[1]-=1
        ans_.append(i+1)
        if ans[1]==0:
            break
print(len(ans_))
print(" ".join(map(str,ans_[::-1])))
