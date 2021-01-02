//Codeforcesで128bit整数を使いたいとき
//→__int128_tを使う&GNU C++17 (64)で提出する
//デバッグ用オプション：-fsanitize=undefined,address

//コンパイラ最適化
#pragma GCC optimize("Ofast")

//インクルードなど
#include<bits/stdc++.h>
using namespace std;
typedef long long ll;

//イテレーション
#define REP(i,n) for(ll i=0;i<ll(n);i++)
#define REPD(i,n) for(ll i=n-1;i>=0;i--)
#define FOR(i,a,b) for(ll i=a;i<=ll(b);i++)
#define FORD(i,a,b) for(ll i=a;i>=ll(b);i--)
#define FORA(i,I) for(const auto& i:I)
//x:コンテナ
#define ALL(x) x.begin(),x.end() 
#define SIZE(x) ll(x.size()) 
//定数
#define INF32 2147483647 //2.147483647×10^{9}:32bit整数のinf
#define INF64 9223372036854775807 //9.223372036854775807×10^{18}:64bit整数のinf
#define MOD 1000000007 //問題による
//略記
#define PB push_back 
#define MP make_pair
#define F first
#define S second
//出力(空白区切りで昇順に)
#define coutALL(x) for(auto i=x.begin();i!=--x.end();i++)cout<<*i<<" ";cout<<*--x.end()<<endl;

//aをbで割る時の繰上げ,繰り下げ
ll myceil(ll a,ll b){return (a+(b-1))/b;}
ll myfloor(ll a,ll b){return a/b;}

//以下、素集合と木は同じものを表す
class UnionFind{
public:
    vector<ll> parent; //parent[i]はiの親
    vector<ll> siz; //素集合のサイズを表す配列(1で初期化)
    map<ll,vector<ll>> group; //集合ごとに管理する(key:集合の代表元、value:集合の要素の配列)
    ll n; //要素数

    //コンストラクタ
    UnionFind(ll n_):n(n_),parent(n_),siz(n_,1){ 
        //全ての要素の根が自身であるとして初期化
        for(ll i=0;i<n;i++){parent[i]=i;}
    }

    //データxの属する木の根を取得(経路圧縮も行う)
    ll root(ll x){
        if(parent[x]==x) return x;
        return parent[x]=root(parent[x]);//代入式の値は代入した変数の値なので、経路圧縮できる
    }

    //xとyの木を併合
    void unite(ll x,ll y){
        ll rx=root(x);//xの根
        ll ry=root(y);//yの根
        if(rx==ry) return;//同じ木にある時
        //小さい集合を大きい集合へと併合(ry→rxへ併合)
        if(siz[rx]<siz[ry]) swap(rx,ry);
        siz[rx]+=siz[ry];
        parent[ry]=rx;//xとyが同じ木にない時はyの根ryをxの根rxにつける
    }

    //xとyが属する木が同じかを判定
    bool same(ll x,ll y){
        ll rx=root(x);
        ll ry=root(y);
        return rx==ry;
    }

    //xの素集合のサイズを取得
    ll size(ll x){
        return siz[root(x)];
    }

    //素集合をそれぞれグループ化
    void grouping(){
        //経路圧縮を先に行う
        REP(i,n)root(i);
        //mapで管理する(デフォルト構築を利用)
        REP(i,n)group[parent[i]].PB(i);
    }

    //素集合系を削除して初期化
    void clear(){
        REP(i,n){parent[i]=i;}
        siz=vector<ll>(n,1);
        group.clear();
    }
};

//辺の構造体
struct Edge{
    ll u,v,cost;
    //後ろにconstつける！
    bool operator<(const Edge& e) const {return this->cost<e.cost;}
};

//クラスカル法
//ret:=最小全域木の重みの総和
//n:=頂点の総数
//計算量:=O(m log{n})
ll Kruskal(vector<Edge> &edges,ll n){
    sort(ALL(edges));//辺の重みの昇順
    UnionFind uf(n);
    ll ret=0;
    FORA(e,edges){
        //その辺を加える必要があるか
        if (!uf.same(e.u,e.v)){
            uf.unite(e.u,e.v);
            ret+=e.cost;
        }
    }
    return ret;
}
//9:23~
signed main(){
    //小数の桁数の出力指定
    //cout<<fixed<<setprecision(10);
    //入力の高速化用のコード
    //ios::sync_with_stdio(false);
    //cin.tie(nullptr);
    ll n;cin>>n;
    vector<tuple<ll,ll,ll>> city1,city2;
    REP(i,n){
        ll x,y;cin>>x>>y;
        city1.PB({x,y,i});
        city2.PB({y,x,i});
    }
    sort(ALL(city1));sort(ALL(city2));
    vector<Edge> edges;
    REP(i,n-1){
        edges.PB({get<2>(city1[i]),get<2>(city1[i+1]),min(abs(get<0>(city1[i])-get<0>(city1[i+1])),abs(get<1>(city1[i])-get<1>(city1[i+1])))});
        edges.PB({get<2>(city2[i]),get<2>(city2[i+1]),min(abs(get<0>(city2[i])-get<0>(city2[i+1])),abs(get<1>(city2[i])-get<1>(city2[i+1])))});
    }
    cout<<Kruskal(edges,n)<<endl;
}