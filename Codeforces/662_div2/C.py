from collections import Counter
for _ in range(int(input())):
    n=int(input())
    s=list(map(int,input().split()))
    d=Counter(s)
    d=list(d.items())
    #print(d)
    d.sort(reverse=True,key=lambda x:x[1])
    l=len(d)
    now=[1,d[0][1]]
    for i in range(1,l):
        if now[1]==d[i][1]:
            now[0]+=1
        else:
            break
    k=now[1]
    m=now[0]
    #print(d)
    print((n-m)//(k-1)-1)