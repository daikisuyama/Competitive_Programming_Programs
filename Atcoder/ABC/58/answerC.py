alp=[chr(i) for i in range(97, 97+26)]
inf=10000000
check=[inf]*26

n=int(input())
for i in range(n):
    s=input()
    ls=len(s)
    check_sub=[0]*26
    for j in range(ls):
        #print(s[j])
        check_sub[alp.index(s[j])]+=1
    for k in range(26):
        check[k]=min(check[k],check_sub[k])
    #print(check_sub)
ans=""
for i in range(26):
    #print(check[i])
    ans+=check[i]*alp[i]
print(ans)
