s=input()
l=len(s)
k=int(input())
alp=[chr(i) for i in range(97, 97+26)]
ans=set()
for i in range(26):
    for j in range(l):
        if s[j]==alp[i]:
            for m in range(j,min(l,j+k)):
                ans.add(s[j:m+1])
    if len(ans)>=k:
        break
print(sorted(list(ans))[k-1])