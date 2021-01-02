//128bit整数はGNU C++17 (64)で出す！
//128bit整数はcastを忘れずに！

//デバッグ用オプション：-fsanitize=undefined,address

//コンパイラ最適化
#pragma GCC optimize("Ofast")

//インクルードなど
#include<bits/stdc++.h>
using namespace std;
typedef __int128_t ll;

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

//aでbを割る時の繰上げ
ll myceil(ll a,ll b){
    return (a+(b-1))/b;
}

/*
二元一次不定方程式(Binary first-order indefinite equation)
初期化すると、x=x0+m*b,y=y0-m*aで一般解が求められる(初めはm=0)
オーバフローする可能性があるので注意！(→禁じ手:Pythonを使う)
*/
struct InEq{
    ll a,b,c,x0,y0;
    ll m=0;
    //解が存在するか
    bool check=true;
    //初期化
    InEq(ll a_,ll b_,ll c_): a(a_),b(b_),c(c_){
        ll g=gcd(static_cast<long long>(a),static_cast<long long>(b));
        if(c%g!=0){
            check=false;
        }else{
            //ax+by=gの特殊解
            extgcd(a,b,x0,y0);
            //ax+by=cの特殊解(掛け算のオーバフローに注意！)
            x0*=c/g;y0*=c/g;
            //一般解を求めるために
            a/=g;b/=g;
        }
    }
    //拡張ユークリッドの互除法
    //返り値:aとbの最大公約数
    ll extgcd(ll a,ll b,ll &x,ll &y){
        if(b==0){
            x=1;
            y=0;
            return a;
        }
        ll d=extgcd(b,a%b,y,x);
        y-=a/b*x;
        return d;
    }
    //パラメータmの更新(xには+bでyには-aの効果)
    void m_update(ll m_){
        x0+=(m_-m)*b;
        y0-=(m_-m)*a;
        m=m_;
    }
};

signed main(){
    //小数の桁数の出力指定
    //cout<<fixed<<setprecision(10);
    //入力の高速化用のコード
    //ios::sync_with_stdio(false);
    //cin.tie(nullptr);
    long long n,p,w,d;cin>>n>>p>>w>>d;
    InEq eq(w,d,p);
    if(!eq.check){
        cout<<-1<<endl;
        return 0;
    }
    if(eq.y0>=0){
        eq.m_update(eq.y0/eq.a);
    }else{
        eq.m_update(-myceil(-eq.y0,eq.a));
    }
    if(eq.x0<0 or eq.x0+eq.y0>n){
        cout<<-1<<endl;
    }else{
        cout<<static_cast<long long>(eq.x0)<<" "<<static_cast<long long>(eq.y0)<<" "<<(n-static_cast<long long>(eq.x0)-static_cast<long long>(eq.y0))<<endl;
    }
}