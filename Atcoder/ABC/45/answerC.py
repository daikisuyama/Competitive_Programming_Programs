s=input()
l=len(s)

ans=0
for i in range(2**(l-1)):
    ans_sub=0
    subst=s[0]
    for j in range(l-1):
        if (i>>j)&1:
            ans_sub+=int(subst)
            subst=s[j+1]
        else:
            subst+=s[j+1]
        if j==l-2:
            ans_sub+=int(subst)
    ans+=ans_sub
if l==1:
    print(int(s))
else:
    print(ans)