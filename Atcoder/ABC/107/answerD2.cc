//インクルード(アルファベット順,bits/stdc++.hは使わない派閥)
#include<algorithm>//sort,二分探索,など
#include<bitset>//固定長bit集合
#include<cmath>//pow,logなど
#include<complex>//複素数
#include<deque>//両端アクセスのキュー
#include<functional>//sortのgreater
#include<iomanip>//setprecision(浮動小数点の出力の誤差)
#include<iostream>//入出力
#include<iterator>//集合演算(積集合,和集合,差集合など)
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
//forループ関係
//引数は、(ループ内変数,動く範囲)か(ループ内変数,始めの数,終わりの数)、のどちらか
//Dがついてないものはループ変数は1ずつインクリメントされ、Dがついてるものはループ変数は1ずつデクリメントされる
#define REP(i,n) for(ll i=0;i<(ll)(n);i++)
#define REPD(i,n) for(ll i=n-1;i>=0;i--)
#define FOR(i,a,b) for(ll i=a;i<=(ll)(b);i++)
#define FORD(i,a,b) for(ll i=a;i>=(ll)(b);i--)
//xにはvectorなどのコンテナ
#define ALL(x) (x).begin(),(x).end() //sortなどの引数を省略したい
#define SIZE(x) ((ll)(x).size()) //sizeをsize_tからllに直しておく
#define MAX(x) *max_element(ALL(x)) //最大値を求める
#define MIN(x) *min_element(ALL(x)) //最小値を求める
//定数
#define INF 1000000000000 //10^12:極めて大きい値,∞
#define MOD 1000000007 //10^9+7:合同式の法
#define MAXR 100000 //10^5:配列の最大のrange(素数列挙などで使用)
//略記
#define PB push_back //vectorヘの挿入
#define MP make_pair //pairのコンストラクタ
#define F first //pairの一つ目の要素
#define S second //pairの二つ目の要素


//1-indexed
class BIT {
public:
    ll n; //データの長さ
    vector<ll> bit; // データの格納先
    BIT(ll n):n(n),bit(n+1,0){} //コンストラクタ

    //bit_i にxをO(log(n))で加算する
    void add(ll i,ll x){
        if(i==0) return;
        for(ll k=i;k<=n;k+=(k & -k)){
            bit[k]+=x;
        }
    }

    //bit_1 + bit_2 + … + bit_n-1 + bit_n をO(log(n))で求める
    ll sum(ll i){
        ll s=0;
        if(i==0) return s;
        for(ll k=i;k>0;k-=(k & -k)){
            s+=bit[k];
        }
        return s;
    }
};

ll solve(vector<ll>& a,ll x,ll n){
    vector<ll> b(n,-1);
    REP(i,n)if(a[i]>=x)b[i]=1;
    vector<ll> s(n+1,0);
    
    //ここ違った…
    FOR(i,1,n)s[i]=s[i-1]+b[i-1];

    ll base=1-MIN(s);REP(i,n+1)s[i]+=base;
    BIT T(MAX(s));
    ll ret=0;
    REP(i,n+1){
        ret+=T.sum(s[i]);
        T.add(s[i],1);
    }
    return ret;
}

signed main(){
    ll n;cin >> n;
    vector<ll> a(n,0);vector<ll> c(n,0);
    REP(i,n){cin >> a[i];c[i]=a[i];}
    sort(ALL(c));c.erase(unique(ALL(c)),c.end());
    //答えを二分探索で探す
    ll check=((n+1)*n/2)/2;
    ll l,r;l=0;r=SIZE(c)-1;
    while(r>l+1){
        ll h=(l+r)/2;
        if(solve(a,c[h],n)>=check){
            l=h;
        }else{
            r=h;
        }
    }
    #if 0
    //デバッグ用コード
    REP(i,SIZE(c)){
        cout << c[i] << " " << solve(a,c[i],n) << endl;
    }
    #endif

    //ここでもlとrを反対にするミス…
    if(solve(a,c[r],n)>=check){
        cout << c[r] << endl;
    }else{
        cout << c[l] << endl;
    }
}