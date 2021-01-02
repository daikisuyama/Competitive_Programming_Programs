n=int(input())
a=[input() for i in range(n)]
a.sort(key=lambda x:len(x))
for i in range(n-1):
    if a[i] not in a[i+1]:
        print("NO")
        break
else:
    print("YES")
    for i in range(n):
        print(a[i])