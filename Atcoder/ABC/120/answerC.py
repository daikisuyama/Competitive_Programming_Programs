#隣あっている二つを除いていくと順番によらずに最後は組みになることができなかったものが残るので
x=0
s=input()
for i in s:
    if i=="0":
        x+=1
    else:
        x-=1
print(len(s)-abs(x))

#もっと短くしたい
print(2*min(map(input().count,"01")))
#0または1の数を数を数えて少ない方を2倍する
#差分で考えるのと違うやり方か
