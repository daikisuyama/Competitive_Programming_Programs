s=input()
n=len(s)
ans=0
for i in range(n):
    if i%2==0:
        if s[i]=="p":
            ans-=1
    else:
        if s[i]=="g":
            ans+=1
print(ans)