#たかだか2019
#かけたら超える可能性があるのか
#問題文読み違えた
#色々ダメすぎる
#意味がわからない
#25分+3ミス、辛い
#なんでこんなんなのか
#掛け算連続した二数だと思った
#掛け算したら2019超える可能性あること忘れてた
#コノママでは甘いぞ
#鍛錬、落ち着いて溶け

l,r=input().split()
l,r=int(l),int(r)
if r-l>=2018:
    print(0)
else:
    '''
    l,r=l%2019,r%2019
    if r>l:
        print(l*(l+1))
    else:
        print(0)
    '''
    '''
    x=(l*(l+1))%2019
    for i in range(l+1,r+1):
        x=min([i*(i+1),x])%2019
        if x==0:
            break
    print(x)
    '''
    a=[i%2019 for i in range(l,r+1)]
    x=(a[0]*a[1])%2019
    for i in range(len(a)):
        for j in range(len(a)-i-1):
            x=min([x,(a[i]*a[i+1+j])%2019])
            if x==0:
                break
        if x==0:
            break
    print(x)
