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

//返り値:aとbの最大公約数
//ax+by=gcd(a,b)を満たす(x,y)が格納される
ll extgcd(ll a,ll b,ll &x,ll &y) {
    if(b==0){
        x=1;
        y=0;
        return a;
    }
    ll d=extgcd(b,a%b,y,x);
    y-=a/b*x;
    return d;
}


signed main(){
    //小数の桁数の出力指定
    //cout<<fixed<<setprecision(10);
    //入力の高速化用のコード
    //ios::sync_with_stdio(false);
    //cin.tie(nullptr);
    ll n,p,w,d;cin>>n>>p>>w>>d;
    if(p%gcd(w,d)!=0){
        cout<<-1<<endl;
        return 0;
    }
    ll f=gcd(w,d);
    ll h=p/f;
    ll x,y;
    extgcd(w,d,x,y);
    //この時点でyは限りなく小さくする(xは大きい)
    x*=h;y*=h;
    // /cout<<x<<" "<<y<<endl;
    w/=f;
    d/=f;
    if(y>=0){
        ll g=y/w;
        x+=g*d;
        y-=g*w;
    }else{
        ll g=(-y+(w-1))/w;
        x-=g*d;
        y+=g*w;
    }
    //cout<<x<<" "<<y<<endl;
    if(x<0 or x+y>n){
        cout<<-1<<endl;
    }else{
        //cout<<x<<endl;
        //cout<<(n-x-y)<<endl;
        cout<<x<<" "<<y<<" "<<(n-x-y)<<endl;
    }
}