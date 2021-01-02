//デバッグ用オプション：-fsanitize=undefined,address

//コンパイラ最適化
#pragma GCC optimize("Ofast")

//インクルードなど
#include<bits/stdc++.h>
using namespace std;
typedef long long ll;

//マクロ
//forループ
//引数は、(ループ内変数,動く範囲)か(ループ内変数,始めの数,終わりの数)、のどちらか
//Dがついてないものはループ変数は1ずつインクリメントされ、Dがついてるものはループ変数は1ずつデクリメントされる
//FORAは範囲for文(使いにくかったら消す)
#define REP(i,n) for(ll i=0;i<ll(n);i++)
#define REPD(i,n) for(ll i=n-1;i>=0;i--)
#define FOR(i,a,b) for(ll i=a;i<=ll(b);i++)
#define FORD(i,a,b) for(ll i=a;i>=ll(b);i--)
#define FORA(i,I) for(const auto& i:I)
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
//計算量:=O(|E|log|V|)
tuple<ll,vector<ll>,vector<pair<ll,ll>>> Kruskal(vector<Edge> &edges,ll n){
    vector<ll> f1;vector<pair<ll,ll>> f2;
    sort(ALL(edges));//辺の重みの昇順
    UnionFind uf=UnionFind(n);
    ll ret=0;
    FORA(e,edges){
        //その辺を加える必要があるか(発電所or辺)
        if (!uf.same(e.u,e.v)){
            uf.unite(e.u,e.v);
            ret+=e.cost;
            if(e.v==n-1){
                f1.PB(e.u+1);
            }else{
                f2.PB(MP(e.u+1,e.v+1));
            }
        }
    }
    return {ret,f1,f2};
}


signed main(){
    //小数の桁数の出力指定
    //cout<<fixed<<setprecision(10);
    //入力の高速化用のコード
    //ios::sync_with_stdio(false);
    //cin.tie(nullptr);
    ll n;cin>>n;
    vector<pair<ll,ll>> xy(n);REP(i,n)cin>>xy[i].F>>xy[i].S;
    vector<ll> c(n);REP(i,n)cin>>c[i];
    vector<ll> k(n);REP(i,n)cin>>k[i];
    vector<Edge> edges;
    REP(i,n){
        FOR(j,i+1,n-1){
            edges.PB({i,j,(abs(xy[i].F-xy[j].F)+abs(xy[i].S-xy[j].S))*(k[i]+k[j])});
        }
    }
    REP(i,n)edges.PB({i,n,c[i]});
    tuple<ll,vector<ll>,vector<pair<ll,ll>>> t=Kruskal(edges,n+1);
    cout<<get<0>(t)<<endl;
    cout<<SIZE(get<1>(t))<<endl;
    REP(i,SIZE(get<1>(t))){
        if(i==SIZE(get<1>(t))-1)cout<<get<1>(t)[i]<<endl;
        else cout<<get<1>(t)[i]<<" ";
    }
    cout<<SIZE(get<2>(t))<<endl;
    REP(i,SIZE(get<2>(t))){
        cout<<get<2>(t)[i].F<<" "<<get<2>(t)[i].S<<endl;
    }
}