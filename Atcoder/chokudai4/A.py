# うーん難しいけど仕方ない
#まだこの段階には至れてないのかな
#いつか至ったら復習
import copy
n,b1,b2,b3=map(int,input().split())

l=[list(map(int,input().split())) for i in range(n)]
r=[list(map(int,input().split())) for i in range(n)]

a=copy.deepcopy(r)#仮の行列を保存しておく,rでもOK
#行と列のそれぞれの和(3の倍数になるように)
c1,c2=[0]*n,[0]*n

for i in range(n):
    e1,e2=0,0
    for j in range(n-i-1):
        for k in range(l[i][i+j],r[i][i+j]+1):
            if (c1[i]+k)%b3==0:
                a[i][i+j]=k
                break
        else:
            for k in range(l[i][i+j],r[i][i+j]+1):
                if (c1[i]+k)%b2==0:
                    a[i][i+j]=k
                    break
            else:
                for k in range(l[i][i+j],r[i][i+j]+1):
                    if (c1[i]+k)%b1==0:
                        a[i][i+j]=k
                        break
        c1[i]+=a[i][i+j]
        c2[i+j]+=a[i][i+j]

        #行の方を計算
        #a[i][i+j]
        #b1[i]+=a[i][i+j]
        if j!=0:
            for k in range(l[i+j][i],r[i+j][i]+1):
                if (c2[i]+k)%b3==0:
                    a[i+j][i]=k
                    break
            else:
                for k in range(l[i+j][i],r[i+j][i]+1):
                    if (c2[i]+k)%b2==0:
                        a[i+j][i]=k
                        break
                else:
                    for k in range(l[i+j][i],r[i+j][i]+1):
                        if (c2[i]+k)%b1==0:
                            a[i+j][i]=k
                            break

            c2[i]+=a[i+j][i]
            c1[i+j]+=a[i+j][i]
        #列の方を計算
        #a[i+j][i]
        #b2[i]+=a[i+j][i]
#print()

for i in range(n):
    for j in range(n):
        #print(l[i][j])
        print(a[i][j],end=" ")
        #print(r[i][j])
    print()

print(l[0])
print(a[0])
print(r[0])
