#nの大きさ見てオーダー決めんと
'''
n=int(input())
a=[]
c=0
for i in range(n):
    a1=int(input())
    if a1 in a:
        c+=1
    else:
        a.append(a1)

print(c)
'''
#これじゃダメか
#内包表記なら
#速さがどんくらいかの感覚がない
#チリも積もれば山感ある
#時間計測
n=int(input())
a=[int(input()) for _ in range(n)]
print(len(a)-len(set(a)))
