#まだ自信をもって答えられないんだよな
#掛け算じゃなくて最小公倍数や
#デバッグの後消す
#30ぷんかかった
#mathモジュールのgcdは使えない
import fractions
a,b,c,d=[int(i) for i in input().split()]
c1=b//c-a//c
if a%c==0:
    c1+=1
d1=b//d-a//d
if a%d==0:
    d1+=1
cd1=b//(c*d//fractions.gcd(c,d))-a//(c*d//fractions.gcd(c,d))
if a%(c*d)==0:
    cd1+=1
#print(c1)
#print(d1)
#print(cd1)
print(b-a+1-c1-d1+cd1)
#役立つhttps://qiita.com/chun1182/items/ddf2b6cba932b2bb0d4e
