//インクルード(アルファベット順)
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

signed main(){
    //入力の高速化用のコード
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    ll n,k,s,t;cin >> n >> k >> s >> t;
    vector<ll> b(n);REP(i,n)cin >> b[i];
    vector<ll> a;
    REP(i,n){
        bool f=true;
        REP(j,18){
            if((s>>j)&1 and !((b[i]>>j)&1)){
                f=false;break;
            }
            if(!((t>>j)&1) and (b[i]>>j)&1){
                f=false;break;
            }
        }
        if(f)a.PB(b[i]);
    }
    n=SIZE(a);
    k=min(n,k);
    //cout << n << endl;
    //cout << n << endl;
    //unordered_mapはpairをキーにできない
    //dp_subを用意すると遅い(用意しないだけで数倍変わる)
    //逆順にやればOK
    vector<map<pair<ll,ll>,ll>> dp(k);
    REP(i,n){
        FORD(j,k-2,0){
            for(auto l=dp[j].begin();l!=dp[j].end();l++){
                dp[j+1][MP((l->F.F)&a[i],(l->F.S)|a[i])]+=(l->S);
            }
        }
        dp[0][MP(a[i],a[i])]=1;
    }
    ll ans=0;
    REP(i,k)ans+=(dp[i][MP(s,t)]);
    cout << ans << endl;
}
