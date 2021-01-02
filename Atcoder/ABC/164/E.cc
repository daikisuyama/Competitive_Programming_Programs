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
//このINFの大きさも重要(小さいとWAに)
#define INF 1000000000000000 //10^15:極めて大きい値,∞
#define MOD 10000007 //10^9+7:合同式の法
#define MAXR 100000 //10^5:配列の最大のrange(素数列挙などで使用)
//略記
#define PB push_back //vectorヘの挿入
#define MP make_pair //pairのコンストラクタ
#define F first //pairの一つ目の要素
#define S second //pairの二つ目の要素

//ここから上はテンプレート

#define VL vector<ll>

//昇順の場合はgreater
//vectorの比較は一つ目の要素二つ目の要素…の優先順位
#define PQ priority_queue<VL,vector<VL>,greater<VL>>
//持つ銀貨の最大の枚数
#define MAXS ll(2999)


//fは始点のインデックス
//nは頂点の総数
//sは最初に持っている通貨の枚数
//edgeはそれぞれの頂点から伸びる辺についてその辺の先の頂点のインデックスおよび減る(or増える)銀貨の枚数およびかかる時間を持つ配列
vector<VL> dijkstra(ll f,ll n,ll s,vector<vector<VL>>& edge){
    //持つ銀貨の枚数は最大でMAXS
    s=min(s,MAXS);
    //それぞれの頂点のそれぞれの通貨の枚数の状態での最短時間が確定済みかをチェックする配列
    vector<VL> confirm(n,VL(MAXS+1,false));
    //それぞれの頂点のそれぞれの通貨の枚数の状態での最短時間を保存する配列
    //始点での初めの状態(通貨はS枚持っている)は0でそれ以外はINFで最短時間を初期化する
    vector<VL> mincost(n,VL(MAXS+1,INF));mincost[f][s]=0;
    //確定済みの(頂点,通貨枚数)の集合から伸びる辺を伝ってたどり着く(頂点,通貨枚数)の始状態からかかる時間を短い順に保存するPriority queue
    PQ mincand;mincand.push({mincost[f][s],f,s});

    //mincandの要素がゼロの時、最短時間を更新できる(頂点,通貨枚数)の状態がないことを示す
    while(!mincand.empty()){
        //最短距離でたどり着くと思われる(頂点,通貨枚数)の状態を取り出す
        VL next=mincand.top();mincand.pop();
        //すでにその(頂点,通貨枚数)の状態の最短時間が確定済みの場合は飛ばす
        if(confirm[next[1]][next[2]]) continue;
        //確定済みではない場合は確定済みにする
        confirm[next[1]][next[2]]=true;
        //確定済みの(頂点,通貨枚数)の状態から伸びる辺の情報をとってくる、lはその辺の本数
        vector<VL>& v=edge[next[1]];ll l=SIZE(v);
        REP(i,l){
            //移動後の銀貨の枚数が何枚になるかを計算する。MAXSを超えた場合はMAXSにする。
            ll nextS=min(next[2]+v[i][1],MAXS);
            //移動後の銀貨の枚数が0より小さいと移動できない
            if(nextS<0) continue;
            //移動した際の時間が辺の先のmincost以上の場合は更新する必要がない(辺の先が確定済みの時はこれを満たす)
            if(mincost[v[i][0]][nextS]<=next[0]+v[i][2]) continue;
            //更新
            mincost[v[i][0]][nextS]=next[0]+v[i][2];
            //更新した場合はその(頂点,通貨枚数)の状態が(確定済みでない(頂点,通貨枚数)の状態の中で)最短距離になる可能性がある
            mincand.push({mincost[v[i][0]][nextS],v[i][0],nextS});
        }
    }
    return mincost;
}

signed main(){
    ll n,m,s;cin >> n >> m >> s;

    vector<vector<VL>> edge(n);
    REP(i,m){
        ll u,v,a,b;cin >> u >> v >> a >> b;
        //ここでは辺は双方向
        edge[u-1].PB({v-1,-a,b});
        edge[v-1].PB({u-1,-a,b});
    }
    REP(i,n){
        ll c,d;cin >> c >> d;
        //通貨を増やす操作もedgeとして加える
        edge[i].PB({i,c,d});
    }
    
    vector<VL> mincost=dijkstra(0,n,s,edge);
    
    FOR(i,1,n-1) cout << MIN(mincost[i]) << endl;
}