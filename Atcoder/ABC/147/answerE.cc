//コンパイラ最適化用
#pragma GCC optimize("Ofast")
//インクルード(アルファベット順)
#include<algorithm>//sort,二分探索,など
#include<bitset>//固定長bit集合
#include<chrono>//実行時間計測
#include<cmath>//pow,logなど
#include<complex>//複素数
#include<deque>//両端アクセスのキュー
#include<functional>//sortのgreater
#include<iomanip>//setprecision(浮動小数点の出力の誤差)
#include<iostream>//入出力
#include<iterator>//集合演算(積集合,和集合,差集合など)
#include<map>//map(辞書)
#include<numeric>//iota(整数列の生成),gcdとlcm,accumulate
#include<queue>//キュー
#include<set>//集合
#include<stack>//スタック
#include<string>//文字列
#include<unordered_map>//順序保持しないmap
#include<unordered_set>//順序保持しないset
#include<utility>//pair
#include<vector>//可変長配列

using namespace std;
typedef long long ll;

//マクロ
//forループ
//引数は、(ループ内変数,動く範囲)か(ループ内変数,始めの数,終わりの数)、のどちらか
//Dがついてないものはループ変数は1ずつインクリメントされ、Dがついてるものはループ変数は1ずつデクリメントされる
#define REP(i,n) for(ll i=0;i<ll(n);i++)
#define REPD(i,n) for(ll i=n-1;i>=0;i--)
#define FOR(i,a,b) for(ll i=a;i<=ll(b);i++)
#define FORD(i,a,b) for(ll i=a;i>=ll(b);i--)
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

signed main(){
    ll h,w;cin>>h>>w;
    vector<vector<ll>> ab(h,vector<ll>(w,0));
    vector<vector<ll>> b(h,vector<ll>(w));
    REP(i,h)REP(j,w)cin>>ab[i][j];
    REP(i,h)REP(j,w){cin>>b[i][j];ab[i][j]-=b[i][j];}
    ll r=2*80*80+1;
    vector<vector<vector<bool>>> dp(h,vector<vector<bool>>(w,vector<bool>(r,false)));
    dp[0][0][abs(ab[0][0])]=true;
    REP(i,h){
        REP(j,w){
            REP(k,r){
                if(dp[i][j][k]){
                    if(i!=h-1)dp[i+1][j][abs(k+ab[i+1][j])]=true;
                    if(i!=h-1)dp[i+1][j][abs(k-ab[i+1][j])]=true;
                    if(j!=w-1)dp[i][j+1][abs(k+ab[i][j+1])]=true;
                    if(j!=w-1)dp[i][j+1][abs(k-ab[i][j+1])]=true;
                }
            }
        }
    }
    REP(k,r)if(dp[h-1][w-1][k]){cout<<k<<endl;return 0;}
}