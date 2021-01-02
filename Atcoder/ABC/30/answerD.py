#まず、ループになるのは明らかそのループを見つけるにはnだけ回せば大丈夫(同じのを見つけたら終了すればいいだけ)
#順番がどうなるかを保存しておく配列とすでに出てきたかどうかを保存する集合(O(1))を用意すれば効率よさそう

n,a=map(int,input().split())
a-=1
k=int(input())
b=[int(i)-1 for i in input().split()]

s=set()
s.add(a)
ans=[a]
for i in range(n):
    nex=b[ans[-1]]
    if nex in s:
        break
    else:
        s.add(nex)
        ans.append(nex)
roop=len(ans)
for i in range(roop):
    if ans[i]==nex:
        start=i
        break
roop-=start
#print(ans)
#print(start)
#print(roop)
if k<roop+start:
    print(ans[k]+1)
else:
    k-=start
    l=k%roop
    print(ans[start+l]+1)