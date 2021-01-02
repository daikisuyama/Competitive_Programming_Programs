//コンパイラ最適化用
#pragma GCC optimize("O3")
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
//.lower_boundはO(√n)
signed main(){
    //入力の高速化用のコード
    //ios::sync_with_stdio(false);
    //cin.tie(nullptr);
    ll n;cin>>n;
    vector<ll> p(n);vector<ll> p_num(n);
    REP(i,n){cin>>p[i];p[i]--;p_num[p[i]]=i;}
    //番兵を入れておくと良い
    //p[i]よりも大きい数のインデックスを保存しておく
    set<ll> s;
    s.insert(-2);s.insert(-1);
    s.insert(n);s.insert(n+1);
    ll ans=0;
    //大きい数から処理
    REPD(i,n){
        //pでのインデックス
        ll j=p_num[i];
        ll l1,l2,r1,r2;
        r1=*(s.upper_bound(j));
        r2=*(++s.upper_bound(j));
        l1=*(--s.lower_bound(j));
        l2=*(--(--s.lower_bound(j)));
        //cout<<l2<<" "<<l1<<" "<<r1<<" "<<r2<<endl;
        if(l1>-1)ans+=((i+1)*(l1-l2)*(r1-j));
        if(r1<n)ans+=((i+1)*(r2-r1)*(j-l1));
        s.insert(j);
    }
    cout<<ans<<endl;
}