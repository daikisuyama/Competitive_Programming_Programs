#絶対値小さくできるか？
#振動しそうなので
from itertools import dropwhile
from collections import deque
n=int(input())
ans=deque([["",n]])
def bfs(d):
    global ans
    l=len(ans)
    for i in range(l):
        x=ans.popleft()
        new1=[x[0]+"0",x[1]]
        if abs(new1[1])<abs((-2)**d):
            ans.append(new1)
        new2=[x[0]+"1",x[1]-(-2)**d]
        if abs(new2[1])<abs((-2)**d):
            ans.append(new2)
    if d!=0:
        bfs(d-1)
bfs(32)
#全探索できるんかーーい、基本
#適当にできるやろっていうのは絶対だめ

for i in ans:
    if i[1]==0:
        ans=list(dropwhile(lambda x:x=="0",i[0]))
        if len(ans)==0:
            print(0)
        else:
            print("".join(ans))
        break