#全て0以上なら順に足していける
#全て0以下または0より大きくすればいいんじゃね？
#絶対値が最も大きいもの考えてその方向で足せば、
#全て0以下または0より大きくに統一できる(最大n-1回)
#全て0以下の場合は右から左に足す(最大n-1回)
#全て0以上の場合は左から右にたす(最大n-1回)
n=int(input())
a=list(map(int,input().split()))
c,d=min(a),max(a)
ans=[]
if abs(c)>abs(d):
    c_=a.index(c)
    for i in range(n):
        if i!=c_ and a[i]>0:
            ans.append(str(c_+1)+" "+str(i+1))
    for i in range(n-1,0,-1):
        ans.append(str(i+1)+" "+str(i))
else:
    d_=a.index(d)
    for i in range(n):
        if i!=d_ and a[i]<0:
            ans.append(str(d_+1)+" "+str(i+1))
    for i in range(n-1):
        ans.append(str(i+1)+" "+str(i+2))
l=len(ans)
print(l)
for i in range(l):
    print(ans[i])