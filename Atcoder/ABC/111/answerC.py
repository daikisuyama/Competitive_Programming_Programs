import collections

n=int(input())
a=list(map(int,input().split()))
a1=[a[2*i] for i in range(n-n//2)]
a2=[a[2*i+1] for i in range(n//2)]
c1=collections.Counter(a1)
c2=collections.Counter(a2)
e1=c1.most_common()
e2=c2.most_common()
d1=e1[0]
d2=e2[0]
#ちゃんと場合分けすればできるけどめんどくさかった
if d1[0]!=d2[0]:
    print(n-d1[1]-d2[1])
elif len(e1)==1 and len(e2)==1:
    print(min(d1[1],d2[1]))
elif len(e1)==1:
    print(min((n//2-d2[1])+d1[1],n//2-e2[1][1]))
elif len(e2)==1:
    print(min((n-n//2-d1[1])+d2[1],n-n//2-e1[1][1]))
else:
    print(n-max(d1[1]+e2[1][1],d2[1]+e1[1][1]))
