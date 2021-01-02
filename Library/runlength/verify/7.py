#同じ文字が連続する場合はその方向に流れていく
#異なる文字があった場合はその間で入れ替わることを繰り返すだけ
#つまり、RLRL…RLとなってR⇄Lの間での移動を繰り返すだけ
#また、偶奇で配置が変わるが今回は偶数の場合を考えれば良い
#RのグループとLのグループに含まれる人数を求めれば簡単に求まる
from itertools import groupby
s=input()
n=len(s)
#R,Lで組にする
g=[len(list(group)) for key,group in groupby(s)]
l=len(g)//2
h=[[g[2*i],g[2*i+1]] for i in range(l)]
check=[0]*n
now=-1
for i in range(l):
    now+=h[i][0]
    #now,now+1が境目
    #境目での変化量
    ch0,ch1=h[i][1]//2+(h[i][0]-h[i][0]//2),h[i][0]//2+(h[i][1]-h[i][1]//2)
    check[now]+=ch0
    check[now+1]+=ch1
    now+=h[i][1]
print(" ".join(map(str,check)))