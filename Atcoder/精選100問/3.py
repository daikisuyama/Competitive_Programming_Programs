#11/25 8:18~8:21
s=input()
n=len(s)
ans=0
for i in range(n):
    for j in range(i,n):
        if all(i in ["A","C","G","T"] for i in s[i:j+1]):
            ans=max(ans,j-i+1)
print(ans)
