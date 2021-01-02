#include<algorithm>//sort,二分探索,など
#include<bitset>//固定長bit集合
#include<cmath>//pow,logなど
#include<complex>//複素数
#include<deque>//両端アクセスのキュー
#include<functional>//sortのgreater
#include<iomanip>//setprecision(浮動小数点の出力の誤差)
#include<iostream>//入出力
#include<map>//map(辞書)
#include<numeric>//iota(整数列の生成),gcdとlcm(c++17)
#include<queue>//キュー
#include<set>//集合
#include<stack>//スタック
#include<string>//文字列
#include<unordered_map>//イテレータあるけど順序保持しないmap
#include<unordered_set>//イテレータあるけど順序保持しないset
#include<utility>//pair
#include<vector>//可変長配列

using namespace std;
typedef long long ll;

//マクロ
#define REP(i,n) for(ll i=0;i<(ll)(n);i++)
#define REPD(i,n) for(ll i=(ll)(n)-1;i>=0;i--)
#define FOR(i,a,b) for(ll i=(a);i<=(b);i++)
#define FORD(i,a,b) for(ll i=(a);i>=(b);i--)
#define ALL(x) (x).begin(),(x).end() //sortなどの引数を省略したい
#define SIZE(x) ((ll)(x).size()) //sizeをsize_tからllに直しておく
#define INF 1000000000000
#define MOD 1000000007
#define PB push_back
#define MP make_pair
#define F first
#define S second
#define MAXRR 1000 //√MAXR以上の数を設定する
#define MAXR 200000

ll fac[MAXR], finv[MAXR], inv[MAXR];

// テーブルを作る前処理
void COMinit() {
    fac[0] = fac[1] = 1;
    finv[0] = finv[1] = 1;
    inv[1] = 1;
    for (ll i = 2; i < MAXR; i++){
        fac[i] = fac[i - 1] * i % MOD;
        inv[i] = MOD - inv[MOD%i] * (MOD / i) % MOD;
        finv[i] = finv[i - 1] * inv[i] % MOD;
    }
}

// 二項係数計算
ll COM(ll n,ll k){
    if (n < k) return 0;
    if (n < 0 || k < 0) return 0;
    return fac[n] * (finv[k] * finv[n - k] % MOD) % MOD;
}


void Prime_factorize(vector<ll>& v,ll n){
    if(n<=1) return;
    ll l=ll(sqrt(n));
    for(ll i=2;i<l+1;i++){
        if(n%i==0){
            Prime_factorize(v,i);Prime_factorize(v,ll(n/i));return;
        }
    }
    v.push_back(n);return;
}

//エラトステネスのやつ加える
//素数ライブラリ整理


signed main(){
    COMinit();
    map<ll,ll> ma;
    ll n,m;cin >> n >> m;
    vector<ll> vp;
    Prime_factorize(vp,m);
    REP(i,SIZE(vp)){
        ma[vp[i]]++;
    }
    ll ans=1;
    for(auto i=ma.begin();i!=ma.end();i++){
        ans*=COM(i->S+(n-1),n-1);
        ans%=MOD;
    }
    cout << ans << endl;
}