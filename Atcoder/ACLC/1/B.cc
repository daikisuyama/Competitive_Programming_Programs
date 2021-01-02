//デバッグ用オプション：-fsanitize=undefined,address

//コンパイラ最適化
#pragma GCC optimize("Ofast")

//インクルードなど
#include<bits/stdc++.h>
using namespace std;
typedef long long ll;

//マクロ
//forループ
//引数は、(ループ内変数,動く範囲)か(ループ内変数,始めの数,終わりの数)、のどちらか
//Dがついてないものはループ変数は1ずつインクリメントされ、Dがついてるものはループ変数は1ずつデクリメントされる
//FORAは範囲for文(使いにくかったら消す)
#define REP(i,n) for(ll i=0;i<ll(n);i++)
#define REPD(i,n) for(ll i=n-1;i>=0;i--)
#define FOR(i,a,b) for(ll i=a;i<=ll(b);i++)
#define FORD(i,a,b) for(ll i=a;i>=ll(b);i--)
#define FORA(i,I) for(const auto& i:I)
//xにはvectorなどのコンテナ
#define ALL(x) x.begin(),x.end() 
#define SIZE(x) ll(x.size()) 
//定数
#define INF 1000000000000 //10^12:∞
#define MOD 1000000007 //10^9+7:合同式の法
#define MAXR 100000 //10^5:配列の最大のrange
//略記
#define PB push_back //挿入
#define MP make_pair //pairのコンストラクタ
#define F first //pairの一つ目の要素
#define S second //pairの二つ目の要素

// 返り値: a と b の最大公約数
// ax + by = gcd(a, b) を満たす (x, y) が格納される
ll extGCD(ll a, ll b, ll &x, ll &y) {
    if(b==0){
        x=1;
        y=0;
        return a;
    }
    ll d=extGCD(b,a%b,y,x);
    y-=a/b*x;
    return d;
}

ll myceil(ll a,ll b){
    return (a+(b-1))/b;
}

ll make_divisors(ll n){
    vector<ll> divisors;//約数を格納する配列
    ll ret=max(n/2-1,1LL);
    FOR(i,1,sqrt(n)){
        if(n%i==0){
            divisors.PB(i);
            if(i!=n/i){
                divisors.PB(n/i);
            }
        }
    }
    FORA(i,divisors){
        ll x0,y0,a,b;a=i;b=n/i;
        if(extGCD(a,-b,x0,y0)!=1)continue;
        if(x0>=0 and y0>=0){
            ll m=min(ll(x0/b),ll(y0/a));
            if(x0-b*m==0 or y0-a*m==0)m--;
            ll x,y;x=a*(x0-b*m);y=b*(y0-a*m);
            ret=min(ret,y);
        }else if(x0<0 and y0<0){
            ll m=max(myceil(-x0,b),myceil(-y0,a));
            if(x0+b*m==0 or y0+a*m==0)m++;
            ll x,y;x=a*(x0+b*m);y=b*(y0+a*m);
            ret=min(ret,y);
        }else if(x0<0){
            ll m=myceil(-x0,b);
            if(x0+b*m==0)m++;
            ll x,y;x=a*(x0+b*m);y=b*(y0+a*m);
            ret=min(ret,y);
        }else{
            ll m=myceil(-y0,a);
            if(y0+a*m==0)m++;
            ll x,y;x=a*(x0+b*m);y=b*(y0+a*m);
            ret=min(ret,y);
        }
    }
    return ret;
}
signed main(){
    ll n;cin>>n;
    cout<<make_divisors(2*n)<<endl;
}