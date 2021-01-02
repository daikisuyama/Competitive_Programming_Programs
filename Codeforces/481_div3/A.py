n=int(input())
a=list(map(int,input().split()))[::-1]
s={a[0]}
ans=[str(a[0])]
for i in range(1,n):
    if a[i] not in s:
        s.add(a[i])
        ans.append(str(a[i]))
print(len(ans))
print(" ".join(ans[::-1]))