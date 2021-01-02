n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
ab=[[a[i],b[i]] for i in range(n)]
#print(ab)
a.sort()
b.sort()


for i in range(n):
    if b[i]<a[i]:
        s="No"
        break
else:
    s="Yes"
    #こっちのNoのパターンを省く
    #最大でもN-1回
    ab.sort(key=lambda x:x[1])
    a2=[ab[i][0] for i in range(n)]

    for i in range(n-1):
        a2[i],a2[i+1]=a2[i+1],a2[i]
        if a2[i]!=a[i]:
            s="No"
            break
print(s)

    #print(a)
    #print(a2)
