#宝石をそれぞれ獲得するがその順番は任意
#bitDP
#制約からbitDPだとNが大きいので無理
#宝石を全部一個以上→宝石一個以外を全てと考える？
#その一個がO(M)、除いた時O(N)で探せるけどO(MN)で無理
#まとめて考える
#ある遺跡で手にいられない宝石は除いたと考えられる→その遺跡のぶんの得点獲得(その範囲をマイナスで記録しておく→maxからminを引けば答えになる)
#その得点はimosで記録できる
#O(M+N)でできる
#OK

n,m=map(int,input().split())
rec=[0]*m
al=0
for i in range(n):
    l,r,s=map(int,input().split())
    l-=1
    r-=1
    rec[l]-=s
    if r<m-1:rec[r+1]+=s
    al+=s
for i in range(1,m):
    rec[i]+=rec[i-1]
for i in range(m):
    rec[i]+=al
print(max(rec))

