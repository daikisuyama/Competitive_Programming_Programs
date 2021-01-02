#貪欲にシミュレートする
#できるだけ小さくなるように
for _ in range(int(input())):
    n,k,l=map(int,input().split())
    d=list(map(int,input().split()))
    seg=[]
    for i in range(n):
        if l-d[i]<0:
            print("No")
            break
        #必ず端が0以上になるように
        seg.append([-min(l-d[i],k),min(l-d[i],k)])
    else:
        #print(seg)
        now=seg[0][0]
        for i in range(1,n):
            if seg[i]==[-k,k]:
                now=seg[i][0]
            else:
                now+=1
                if now<seg[i][0]:
                    now=seg[i][0]
                elif now>seg[i][1]:
                    print("No")
                    break
        else:
            print("Yes")
