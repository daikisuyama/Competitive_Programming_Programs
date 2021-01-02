from collections import Counter
n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
#0,1,…の余りで並び替える
#aはこれに一致するようにずらすだけ
#高々n回
c=sorted([list(i) for i in list(Counter(a).items())],key=lambda x:x[0])
d=sorted([list(i) for i in list(Counter(b).items())],key=lambda x:x[0])
n=len(c)
#後ろを削除して前にくっつける(差分管理)
x=0
for i in range(n):
    #print(c,d)
    p=c.pop(-1)
    #一周させる必要ない可能性も
    dp=d[0][0]+m-p[0]
    x+=dp
    c.insert(0,p)
    #print(c,d)
    for j in range(n):
        c[j][0]+=dp
        c[j][0]%=m
    if c==d:
        print(x%m)
        break



