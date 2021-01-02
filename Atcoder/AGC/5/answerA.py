x=input()
f=0
#なかなか良い解法、flag立てる
#stackでやるらしい
#こういう問題は最後どんな感じかを実験する
for i in x:
    if i=="S":
        f+=1
    elif f!=0:
        f-=1
print(2*f)
