#めっちゃ時間かかった
#多重キーのソート
N=int(input())
dic=[]
for i in range(N):
    S,P=input().split()
    P=int(P)
    dic.append((i+1,S,P))
dic.sort(key=lambda x:(x[1],-x[2]))

for i in dic:
    print(i[0])



#https://pashango-p.hatenadiary.org/entry/20090614/1244984058
