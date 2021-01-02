n=int(input())
a=[set(input()) for i in range(n)]
ans=[""]*n
for i in range((n-1)//2+1):
    for j in a[i]:
        if j in a[n-i-1]:
            ans[i]=j
            ans[n-i-1]=j
            break
    else:
        print(-1)
        break
else:
    print("".join(ans))
