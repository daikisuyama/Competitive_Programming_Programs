n=int(input())
s=input()
check=dict()
for i in range(n-1):
    t=s[i:i+2]
    if t in check:
        check[t]+=1
    else:
        check[t]=1
c=list(check.items())
c.sort(key=lambda x:x[1],reverse=True)
print(c[0][0])