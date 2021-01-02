n,x=map(int,input().split())
d=list(map(int,input().split()))
a=[i*(i+1)//2 for i in d]
inf=100000000000
ans=0
#now1:どこまで完全にとったか(完全にとってない時-1)
now1=inf
#now2:完全にとった部分の合計は？
now2=0
#add1:追加でどのくらいとったか
add1=0
#add2:追加でとった部分の合計は？
add2=0
for i in range(n-1,-1,-1):
    if now1==inf or now1==i+1:
        check=x
        now1=inf
        now2=0
        add1=0
        add2=0
        if check<d[i]:
            #now1は動かん
            now2=0
            add1=check
            add2=(2*d[i]-check+1)*check//2
        else:
            now1=i
            now2=a[i]
            check-=d[i]
            while check>=d[now1-1]:
                check-=d[now1-1]
                now2+=a[now1-1]
                now1-=1
            add1=check
            add2=(2*d[now1-1]-check+1)*check//2
    else:
        #とってる時は削除
        #checkは追加でとる値
        check=add1+d[i+1]
        add1=0
        add2=0
        now2-=a[i+1]
        if check<d[now1-1]:
            #now1は動かん
            add1=check
            add2=(2*d[now1-1]-check+1)*check//2
        else:
            while check>=d[now1-1]:
                check-=d[now1-1]
                now2+=a[now1-1]
                now1-=1
            add1=check
            add2=(2*d[now1-1]-check+1)*check//2
    #print(now1,now2,add1,add2)
    ans=max(now2+add2,ans)
print(ans)
