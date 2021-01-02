#アンバランスな文字列がある時、できるだけ短いものを考えれば良い
#長さが2以上の時2つ以上連続するものがあるかを探せば良い
#逆にない場合はアンバランスな文字列は存在し得ない
#コーナーケース:aba
#全て長さが1:交互に挟むパターンだけ
from itertools import groupby
s=input()
n=len(s)
x=[[key,len(list(group))] for key,group in groupby(s)]
now=0
for i in x:
    if i[1]>=2:
        print(now+1,now+i[1])
        break
    now+=i[1]
else:
    now=0
    for i in range(1,len(x)-1):
        if x[i-1][0]==x[i+1][0]:
            print(i,i+2)
            break
    else:
        print(-1,-1)