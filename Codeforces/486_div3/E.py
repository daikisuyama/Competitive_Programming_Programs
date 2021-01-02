#死んじゃう
n=[int(i) for i in input()]
l=len(n)
#長さが2の場合も
if len(n)==1:
    print(-1)
    exit()
#これだけの場合
if n in [[2,5],[7,5],[5,0]]:
    print(0)
    exit()
if n in [[5,2],[5,7]]:
    print(1)
    exit()
inf=10**12
#一番左にある場合はめんどいので場合分けしちゃう(逆にする)
#00も場合分け
def calc1(x,y):
    m=n[::-1]
    if x not in n or y not in n:
        #print(x,y,0)
        return inf
    ix,iy=m.index(x),m.index(y)
    #一番右にない場合
    if max(ix,iy)<l-1:
        if iy<ix:
            #print(x,y,1)
            return iy+(ix-1)
        else:
            #print(x,y,2)
            return iy+(ix-1)+1
    else:
        ret=0
        #print(ix,iy)
        if ix==l-1:
            #右から探して左を見る(0かつ他の選択するやつでない)
            for i in range(l-2,-1,-1):
                if m[i]!=0 and i!=iy:
                    break
            else:
                #print(x,y,3)
                return inf
            if i<iy:
                iy-=1
                ret+=(l-1-i)
                ix-=1
                ret+=(iy+(ix-1))
                #print(x,y,4,ret)
                return ret
            else:
                ret+=iy
                ret+=(l-1-i)
                ix-=1
                ret+=(ix-1)
                #print(x,y,5,ret)
                return ret
        else:
            #右から探して左を見る(0かつ他の選択するやつでない)
            #他の選択するやつだけの可能性(最初に排除)
            #外でやる
            for i in range(l-2,-1,-1):
                if m[i]!=0 and i!=ix:
                    break
            else:
                #print(x,y,6)
                return inf
            if i<ix:
                iy-=1
                ret+=(l-1-i)
                ix-=1
                ret+=(iy+(ix-1)+1)
                #print(x,y,7,ret)
                return ret
            else:
                ret+=iy
                ret+=(l-1-i)
                ix-=1
                ret+=((ix-1)+1)
                #print(x,y,8,ret)
                return ret
#00の時
def calc2(x,y):
    #一番右には絶対ない
    if n.count(0)<2:
        return inf
    m=[l-1-i for i in range(l) if n[i]==0][::-1]
    return m[0]+m[1]-1

ans=min([calc1(2,5),calc1(7,5),calc1(5,0),calc2(0,0)])
#print([calc1(2,5),calc1(7,5),calc1(5,0),calc2(0,0)])
print(-1 if ans==inf else ans)