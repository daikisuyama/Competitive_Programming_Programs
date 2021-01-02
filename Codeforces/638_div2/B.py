from collections import deque
for _ in range(int(input())):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    if len(set(a))>k:
        print(-1)
        continue
    ans=[]
    for i in set(a):
        ans.append(str(i))
    for i in range(k-len(set(a))):
        ans.append(str(a[i]))
    realans=[]
    for i in range(n):
        realans+=ans
    print(len(realans))
    print(" ".join(realans))