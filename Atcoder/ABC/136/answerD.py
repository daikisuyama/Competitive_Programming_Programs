#LとRが変わる点に着目
#その点でどちらに行くかを繰り返す
#lの連続しているところの一番左に行く、rの連続しているところの右に行く
#偶数と奇数の時で変わりそう
#二つ入れた時にその繰り返しになったら止めれば良さそう
#二回を繰り返しの単位としてその二回でできたものが同じになっていれば終了
#deepcopyは使うなあほ
import copy
s=input()
n=len(s)

def make_new_list(a_1,a_2):
    for i in range(n):
        if s[i]=="L":
            a_2[i-1]+=a_1[i]
        else:
            a_2[i+1]+=a_1[i]



a0=[1]*n
a1=[0]*n
make_new_list(a0,a1)
a2=[0]*n
make_new_list(a1,a2)
a3=[0]*n
make_new_list(a2,a3)
a4=[0]*n
make_new_list(a3,a4)

while a1!=a3 or a2!=a4:
    a1=copy.deepcopy(a3)
    a2=copy.deepcopy(a4)
    a3=[0]*n
    make_new_list(a2,a3)
    a4=[0]*n
    make_new_list(a3,a4)

print(" ".join(list(map(str,a4))))
