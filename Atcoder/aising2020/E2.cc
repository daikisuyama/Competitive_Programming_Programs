//コンパイラ最適化用
#pragma GCC optimize("Ofast")
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
#define REP(i,n) for(ll i=0;i<ll(n);i++)
#define REPD(i,n) for(ll i=n-1;i>=0;i--)
#define FOR(i,a,b) for(ll i=a;i<=ll(b);i++)
#define FORD(i,a,b) for(ll i=a;i>=ll(b);i--)
//xにはvectorなどのコンテナ
#define ALL(x) x.begin(),x.end() //sortなどの引数を省略したい
#define SIZE(x) ll(x.size()) //sizeをsize_tからllに直しておく
//定数
#define INF 1000000000000 //10^12:極めて大きい値,∞
#define MOD 1000000007 //10^9+7:合同式の法
#define MAXR 100000 //10^5:配列の最大のrange(素数列挙などで使用)
//略記
#define PB push_back //vectorヘの挿入
#define MP make_pair //pairのコンストラクタ
#define F first //pairの一つ目の要素
#define S second //pairの二つ目の要素
#define Umap unordered_map
#define Uset unordered_set

signed main(){
    //入力の高速化用のコード
    //ios::sync_with_stdio(false);
    //cin.tie(nullptr);
    ll t;cin>>t;
    REP(_,t){
        ll n;cin>>n;
        vector<pair<ll,ll>> candl,candr;
        //選ばれていないインデックスを保存しておく
        set<ll> memol,memor;
        REP(i,n){memol.insert(i);memor.insert(i);}
        ll ans=0;
        REP(i,n){
            ll K,L,R;cin>>K>>L>>R;
            if(L>R){ans+=R;candl.PB({L-R,K-1});}
            else if(R>L){ans+=L;candr.PB({R-L,K});}
            else{ans+=L;}
        }
        //降順でソートしておく
        sort(ALL(candl),greater<pair<ll,ll>>());sort(ALL(candr),greater<pair<ll,ll>>());
        ll sl=SIZE(candl);ll sr=SIZE(candr);
        REP(i,sl){
            auto now=memol.upper_bound(candl[i].S);
            if(now!=memol.begin()){memol.erase(--now);ans+=candl[i].F;}
            //else{cout<<candl[i].F<<endl;}
        }
        REP(i,sr){
            auto now=memor.lower_bound(candr[i].S);
            if(now!=memor.end()){memor.erase(now);ans+=candr[i].F;}
            //else{cout<<candr[i].F<<endl;}
        }
        cout<<ans<<endl;
    }
}
