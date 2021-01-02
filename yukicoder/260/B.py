n=int(input())
s,t=map(int,input().split())
s-=1
t-=1
a=list(map(int,input().split()))
s2,t2=[sum(a[:n-(n//2)])],[sum(a[:(n//2)])]
def ind(i):
    return i if i<n else i-n
for i in range(n-1):
    s2.append(s2[-1]-a[i]+a[ind(n-(n//2)+i)])
    t2.append(t2[-1]-a[i]+a[ind(n//2+i)])
ans=[]
#sのスタートを決める
#tのスタートはn-(n//2)だけあと
for i in range(n):
    #sはtを含まない、逆も然り
    #sはtよりもすぐ到達は選択可能
    if (s-i+1 if i<=s else )<=n-(n//2):
