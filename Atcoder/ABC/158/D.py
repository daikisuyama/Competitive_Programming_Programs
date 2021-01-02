from collections import deque
s=input()
q=int(input())
#反転操作はまとめてする
#2の操作が入れ替わるだけ
check=True
d=deque(list(s))
for i in range(q):
    x=input().split()
    if len(x)==1:
        check=(not check)
    else:
        t,f,c=x
        f=int(f)
        if check:
            if f==1:
                d.appendleft(c)
                #s=c+s
            else:
                d.append(c)
                #s=s+c
        else:
            if f==2:
                d.appendleft(c)
                #s=c+s
            else:
                d.append(c)
                #s=s+c

if check:
    print("".join(list(d)))
else:
    print("".join(list(d)[::-1]))