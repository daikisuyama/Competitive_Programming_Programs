#heapqすら使わなくても良い
x,y,a,b,c=map(int,input().split())

p=sorted(list(map(int,input().split())),reverse=True)[:x]
q=sorted(list(map(int,input().split())),reverse=True)[:y]
r=sorted(list(map(int,input().split())),reverse=True)

p.extend(q)
ans=sorted(p)

#ansは小さい順、rは大きい順
for i in range(x+y):
    if len(r)==i or r[i]<ans[i]:
        break
    else:
        ans[i]=r[i]
print(sum(ans))