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

#define PLL pair<ll,ll>
#define VLL vector<ll>
//昇順の場合はgreater
//pairの比較は一つ目の要素→二つ目の要素の優先順位
#define PQ priority_queue<VLL,vector<VLL>,greater<VLL>>


//fは始点のインデックス
//nは頂点の総数
//edgeはそれぞれの頂点から伸びる辺についてその辺の先の頂点のインデックスおよび距離を持つ配列
//1からの最小距離でたどり着いたところにその前のやつ保存
pair<vector<ll>,vector<ll>> dijkstra(ll f,ll n,vector<vector<PLL>>& edge){
    //最短経路としてどの頂点が確定済みかをチェックする配列
    vector<ll> confirm(n,false);
    //それぞれの頂点への最短距離を保存する配列
    //始点は0,始点以外はINFで最短距離を初期化する
    vector<ll> mincost(n,INF);mincost[f]=0;
    vector<ll> signpost(n,-1);
    //確定済みの頂点の集合から伸びる辺を伝ってたどり着く頂点の始点からの距離を短い順に保存するPriority queue
    //どっからきたかも必要か
    vector<ll> data={mincost[f],f,0};
    PQ mincand;mincand.push(data);signpost[f]=0;

    //mincandの要素がゼロの時、最短距離を更新できる頂点がないことを示す
    while(!mincand.empty()){
        //最短距離でたどり着くと思われる頂点を取り出す
        VLL next=mincand.top();mincand.pop();
        //すでにその頂点への最短距離が確定済みの場合は飛ばす
        if(confirm[next[1]]) continue;
        //確定済みではない場合は確定済みにする
        confirm[next[1]]=true;
        //道標決定
        signpost[next[1]]=next[2];
        //その確定済みの頂点から伸びる辺の情報をとってくる(参照の方が速い)、lは辺の本数
        vector<PLL>& v=edge[next[1]];ll l=SIZE(v);
        REP(i,l){
            //辺の先が確定済みなら更新する必要がない((✳︎2)があれば十分なので(✳︎1)は実はいらない)
            if(confirm[v[i].F]) continue; //(✳︎1)
            //辺の先のmincost以上の場合は更新する必要がない(辺の先が確定済みの時は満たす)
            if(mincost[v[i].F]<=next[0]+v[i].S) continue; //(✳︎2)
            //更新
            mincost[v[i].F]=next[0]+v[i].S;
            //更新した場合はその頂点が(確定済みでない頂点の中で)最短距離になる可能性があるのでmincandに挿入
            vector<ll> data_sub={mincost[v[i].F],v[i].F,next[1]};
            mincand.push(data_sub);
        }
    }
    return MP(mincost,signpost);
}

signed main(){
    ll n,m;cin >> n >> m;

    vector<vector<PLL>> edge(n);
    REP(i,m){
        ll a,b;cin >> a >> b;
        edge[a-1].PB(MP(b-1,1));
        edge[b-1].PB(MP(a-1,1));//逆向きの辺も挿入
    }

    pair<vector<ll>,vector<ll>>vv=dijkstra(0,n,edge);

    ll ans=0;
    if(find(ALL(vv.S),-1)==(vv.S).end()){
        cout << "Yes" << endl;
        REP(i,n-1) cout << (vv.S)[i+1]+1 << endl;
    }else{
        cout << "No" << endl;
    }
}