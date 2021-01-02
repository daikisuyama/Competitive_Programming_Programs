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
//#define REPD(i,n) for(ll i=n-1;i>=0;i--)
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

ll n;vector<pair<ll,ll>> vw;vector<vector<ll>> dp;
ll c1,c2;

void dfs(ll i){
    if(i==1){
        dp[i-1][vw[i-1].S]=vw[i-1].F;
    }else{
        ll j=i/2;
        FORD(k,c2,0){
            if(dp[j-1][k]!=0 or k==0){
                ll ne=k+vw[i-1].S;
                if(ne<=c2)dp[i-1][ne]=max(dp[j-1][k]+vw[i-1].F,dp[i-1][ne]);
            }
            dp[i-1][k]=dp[j-1][k];
        }
    }
    if(i*2<=c1 and i*2<=n)dfs(i*2);
    if(i*2+1<=c1 and i*2+1<=n)dfs(i*2+1);
}

signed main(){
    //入力の高速化用のコード
    //ios::sync_with_stdio(false);
    //cin.tie(nullptr);
    cin>>n;
    vw.resize(n);
    REP(i,n)cin>>vw[i].F>>vw[i].S;
    c1=1<<10;c2=100000;
    dp.resize(c1);REP(i,c1)dp[i].resize(c2+1);
    dfs(1);//cout << 1 << endl;
    REP(i,c1)REP(j,c2)dp[i][j+1]=max(dp[i][j],dp[i][j+1]);
    ll q;cin>>q;
    #if 1
    REP(i,q){
        ll v,l;cin>>v>>l;
        vector<ll> cand;
        while(v>c1){
            cand.PB(v);
            v=v/2;
        }
        ll r=SIZE(cand);//cout << r << endl;
        ll ans=0;
        REP(j,1<<r){
            ll v_sub=0;ll w_sub=0;
            REP(k,r){
                if((j>>k)&1){
                    v_sub+=vw[cand[k]-1].first;
                    w_sub+=vw[cand[k]-1].second;
                }
            }
            if(w_sub<=l)ans=max(ans,dp[v-1][l-w_sub]+v_sub);
        }
        cout<<ans<<endl;
    }
    #endif
}