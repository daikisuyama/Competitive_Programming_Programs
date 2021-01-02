n=int(input())
red=sorted([list(map(int,input().split())) for i in range(n)],key=lambda x:x[1],reverse=True)
blue=sorted([list(map(int,input().split())) for i in range(n)])
ans=0
for bx,by in blue:
    for rx,ry in red:
        if rx<bx and ry<by:
            ans+=1
            red.remove([rx,ry])
            break
print(ans)
