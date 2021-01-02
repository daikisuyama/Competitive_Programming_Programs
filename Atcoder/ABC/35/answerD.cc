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
#define MOD 10000007 //10^9+7:合同式の法
#define MAXR 100000 //10^5:配列の最大のrange(素数列挙などで使用)
//略記
#define PB push_back //vectorヘの挿入
#define MP make_pair //pairのコンストラクタ
#define F first //pairの一つ目の要素
#define S second //pairの二つ目の要素

//ここから上はテンプレート

//昇順の場合はgreater
//pairの比較は一つ目の要素→二つ目の要素の優先順位
#define PQ priority_queue<vector<ll>,vector<vector<ll>>,greater<vector<ll>>>


//fは始点のインデックス
//nは頂点の総数
//edgesはそれぞれの頂点から伸びる辺の情報(辺の先とその距離)を持つ配列
vector<ll> dijkstra(ll f,ll n,vector<vector<vector<ll>>>& edges){
    //(1)
    //それぞれの頂点への最短距離を保存する配列
    //まずはINFで初期化する
    vector<ll> mincost(n,INF);
    //確定済みの頂点の集合から伸びる辺の先の頂点の始点からの距離を短い順に保存するPriority queue
    //始点からの自身への距離を0として初期化
    PQ mincand;mincand.push({0,f});
    //(2)
    //mincandの要素がない時、最短距離を更新できる頂点はない
    while(!mincand.empty()){
        //(3)
        //最短距離でたどり着くと"思われる"頂点を取り出す
        vector<ll> next=mincand.top();mincand.pop();
        //その頂点への最短距離が確定済みの場合は飛ばす
        if(mincost[next[1]]<=next[0]) continue;
        //確定していない場合はここで更新する
        mincost[next[1]]=next[0];
        //(4)
        //確定済みの頂点から伸びる辺の情報をとる
        for(const auto& edge:edges[next[1]]){
            //その頂点への最短距離を更新できない場合は飛ばす
            if(mincost[edge[0]]<=next[0]+edge[1]) continue;
            //更新した場合はその頂点への最短距離になる"可能性がある"のでmincandに挿入
            mincand.push({next[0]+edge[1],edge[0]});
        }
    }
    return mincost;
}

signed main(){
    ll n,m;cin >> n >> m;
    ll T;cin >> T;//頂点の数と辺の数
    vector<ll> a(n);REP(i,n) cin >> a[i];

    vector<vector<vector<ll>>> edges(n);
    vector<vector<vector<ll>>> edges_(n);
    REP(i,m){
        ll a,b,c;cin >> a >> b >> c;
        edges[a-1].PB({b-1,c});
        edges_[b-1].PB({a-1,c});//逆向きの辺も挿入
    }

    vector<ll> mincost=dijkstra(0,n,edges);
    vector<ll> mincost_=dijkstra(0,n,edges_);

    ll ans=0;
    REP(i,n) ans=max(ans,(T-mincost[i]-mincost_[i])*a[i]);
    cout << ans << endl;
}
