//デバッグ用オプション：-fsanitize=undefined,address

//コンパイラ最適化
#pragma GCC optimize("Ofast")

//インクルードなど
#include<bits/stdc++.h>
using namespace std;
typedef int ll;

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
    ll n; //要素数

    //コンストラクタ
    UnionFind(ll n_):n(n_),parent(n_),siz(n_,1){ 
        //全ての要素の根が自身であるとして初期化
        for(ll i=0;i<n;i++){parent[i]=i;}
    }

    //データxの属する木の根を取得(経路圧縮も行う)
    ll inline root(ll x){
        if(parent[x]==x) return x;
        return parent[x]=root(parent[x]);//代入式の値は代入した変数の値なので、経路圧縮できる
    }

    //xとyの木を併合
    void inline unite(ll x,ll y){
        ll rx=root(x);//xの根
        ll ry=root(y);//yの根
        if(rx==ry) return;//同じ木にある時
        //小さい集合を大きい集合へと併合(ry→rxへ併合)
        if(siz[rx]<siz[ry]) swap(rx,ry);
        siz[rx]+=siz[ry];
        parent[ry]=rx;//xとyが同じ木にない時はyの根ryをxの根rxにつける
    }

    //xとyが属する木が同じかを判定
    bool inline same(ll x,ll y){
        ll rx=root(x);
        ll ry=root(y);
        return rx==ry;
    }
};

typedef tuple<ll,ll,ll> td;

ll n;
pair<ll,ll> xy[101];
UnionFind uf(105);
td edges[5500];


signed main(){
    cout<<fixed<<setprecision(10);
    scanf("%d",&n);
    vector<pair<ll,ll>> xy(n);
    REP(i,n)scanf("%d%d",&xy[i].F,&xy[i].S);
    ll now=0;
    REP(i,n){
        edges[now]={(100-xy[i].S)*(100-xy[i].S),i,n};
        now++;
        edges[now]={(xy[i].S+100)*(xy[i].S+100),i,n+1};
        now++;
        FOR(j,i+1,n-1){
            ll k=(xy[i].F-xy[j].F)*(xy[i].F-xy[j].F);
            ll l=(xy[i].S-xy[j].S)*(xy[i].S-xy[j].S);
            edges[now]={k+l,i,j};
            now++;
        }
    }
    sort(edges,edges+now,[](const td& l,const td& r){return get<0>(l)<get<0>(r);});
    REP(i,now){
        uf.unite(get<1>(edges[i]),get<2>(edges[i]));
        if(uf.same(n,n+1)){
            cout<<sqrt(get<0>(edges[i]))/2<<endl;
            break;
        }
    }
}