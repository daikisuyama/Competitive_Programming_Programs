#また長さが1の時を考慮していない
#出来るだけループの外で計算する
#三回ミス(こういうのを避ける、ミスった後のカバー)
n=int(input())
a=[int(input()) for i in range(n)]
m1=max(a)
m2=sorted(a,reverse=True)[1]
for i in range(n):
    if m1==a[i]:
        print(m2)
    else:
        print(m1)
