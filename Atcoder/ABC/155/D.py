n,k=map(int,input().split())
a=list(map(int,input().split()))
#b1,b3はそれぞれ絶対値の大きい順に並ぶ
b1=sorted([i for i in a if i<0])
l1=len(b1)
b2=sorted([i for i in a if i==0])
l2=len(b2)
b3=sorted([i for i in a if i>0],reverse=True)
l3=len(b3)
def countk1(x,b11,b13):#x以下になるものの個数
    ret=0
    for i in range(l1):
        lx,rx=0,l3-1
        while lx+1<rx:
            if b13[(lx+rx)//2]*b11[i]<=x:
                lx=(lx+rx)//2
            else:
                rx=(lx+rx)//2
        if b13[rx]*b11[i]<=x:
            ret+=(rx+1)
        elif b13[lx]*b11[i]<=x:
            ret+=(lx+1)
    return ret

def countk2(x,b21,b23):
    #ここ数えすぎ
    ret=0
    for i in range(l1-1):
        lx,rx=i+1,l1-1
        while lx+1<rx:
            if b21[(lx+rx)//2]*b21[i]<=x:
                lx=(lx+rx)//2
            else:
                rx=(lx+rx)//2
        if b21[rx]*b21[i]<=x:
            ret+=(rx-i)
        elif b21[lx]*b21[i]<=x:
            ret+=(lx-i)
    for i in range(l3-1):
        lx,rx=i+1,l3-1
        while lx+1<rx:
            if b23[(lx+rx)//2]*b23[i]<=x:
                lx=(lx+rx)//2
            else:
                rx=(lx+rx)//2
        if b23[rx]*b23[i]<=x:
            ret+=(rx-i)
        elif b23[lx]*b23[i]<=x:
            ret+=(lx-i)
    return ret

if k<=l1*l3:
    l,r=b1[0]*b3[0],-1
    while l+1<r:
        if countk1((l+r)//2,b1,b3)>=k: #k以上、数が存在するかどうか
            r=(l+r)//2
        else:
            l=(l+r)//2
    if countk1(l,b1,b3)==k:
        print(l)
    else:
        print(r)
elif k<=l1*l3+l2*(l1+l3)+(l2*(l2-1))//2:
    print(0)
else:
    k-=(l1*l3+l2*(l1+l3)+(l2*(l2-1))//2)
    l=1
    if l1>=2 and l3<2:
        r=b1[0]*b1[1]
    elif l1<2 and l3>=2:
        r=b3[0]*b3[1]
    else:
        r=max(b1[0]*b1[1],b3[0]*b3[1])
    while l+1<r:
        if countk2((l+r)//2,sorted(b1,reverse=True),sorted(b3))>=k: #k以上、数が存在するかどうか
            r=(l+r)//2
        else:
            l=(l+r)//2
    if countk2(l,sorted(b1,reverse=True),sorted(b3))==k:
        print(l)
    else:
        print(r)