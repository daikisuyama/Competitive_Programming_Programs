#これ間違い
n,m=map(int,input().split())
a=[[int(j) for j in input()] for i in range(n)]
#2,2の場合の関数を考える
#3,3の場合も二回呼び出すだけ
#times
def calc(b,times,base):
    if (sum(b[0][:2])+sum(b[1][:2]))%2==1:
        ans=0
        for i in range(2,n):
            if (sum(b[i][:2])+sum(b[i-1][:2]))%2==0:
                b[i][0]=1-b[i][0]
                ans+=1
        if times!=1:
            return ans+base
        else:
            return calc([i[1:] for i in b],0,ans)
    else:
        b1=[i for i in b]
        b2=[i for i in b]
        ans1,ans2=1,1
        b1[1][0]=1-b1[1][0]
        b2[0][0]=1-b2[0][0]
        for i in range(2,n):
            if (sum(b1[i][:2])+sum(b1[i-1][:2]))%2==0:
                b1[i][0]=1-b1[i][0]
                ans1+=1
        for i in range(2,n):
            if (sum(b2[i][:2])+sum(b2[i-1][:2]))%2==0:
                b2[i][0]=1-b2[i][0]
                ans2+=1
        if times!=1:
            return min(ans1,ans2)+base
        else:
            return min(calc([i[1:] for i in b1],0,ans1),calc([i[1:] for i in b2],0,ans2))
if n>=4 and m>=4:
    print(-1)
    exit()
if n==1 or m==1:
    print(0)
    exit()
if n==2 or m==2:
    #mが2になるように
    if n==2:
        n,m=m,n
        b=[list(x) for x in zip(*a)]
    else:
        b=[i for i in a]
    print(calc(b,0,0))
if n==3 or m==3:
    #mが3になるように
    if n==3:
        n,m=m,n
        b=[list(x) for x in zip(*a)]
    else:
        b=[i for i in a]
    print(calc(b,1,0))