//参考：http://ehafib.hatenablog.com/entry/2015/12/23/164517
//インクルード
#include<algorithm>//sort,二分探索,など
#include<bitset>//固定長bit集合
#include<cmath>//pow,logなど
#include<complex>//複素数
#include<deque>//両端アクセスのキュー
#include<functional>//sortのgreater
#include<iomanip>//setprecision(浮動小数点の出力の誤差)
#include<iostream>//入出力
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
#define REP(i,n) for(ll i=0;i<(ll)(n);i++)
#define REPD(i,n) for(ll i=(ll)(n)-1;i>=0;i--)
#define FOR(i,a,b) for(ll i=(a);i<=(b);i++)
#define FORD(i,a,b) for(ll i=(a);i>=(b);i--)
#define ALL(x) (x).begin(),(x).end() //sortなどの引数を省略したい
#define FORALL(i,x) for(auto i=x.begin();i!=x.end();i++)
#define SIZE(x) ((ll)(x).size()) //sizeをsize_tからllに直しておく
#define MAX(x) *max_element(ALL(x))
#define INF 1000000000000
#define MOD 10000007
#define PB push_back
#define MP make_pair
#define F first
#define S second


class UnionFind {
public:
    vector<ll> parent; //parent[i]はiの親
    vector<ll> siz; //素集合のサイズを表す配列(1で初期化)

    //コンストラクタの:の後ろはメンバ変数を初期化している
    UnionFind(ll n):parent(n),siz(n,1){ //最初は全てが根であるとして初期化する
        for(ll i=0;i<n;i++){parent[i]=i;}
    }

    ll root(ll x){ //データxの属する木の根を再帰で得る
        if(parent[x]==x) return x;
        //代入式の値は代入した変数の値になる！
        //経路圧縮(根に直接要素を繋ぐことで計算を効率化する)
        return parent[x]=root(parent[x]);
        //再帰で得る際に親の更新を行っておく
    }

    void unite(ll x,ll y){ //xとyの木を併合する
        ll rx=root(x);//xの根をrx
        ll ry=root(y);//yの根をry
        if(rx==ry) return; //同じ木にある時
        //小さい集合を大きい集合へと併合させる(ry→rxへ併合)
        if(siz[rx]<siz[ry]) swap(rx,ry);
        siz[rx]+=siz[ry];
        parent[ry]=rx; //xとyが同じ木にない時はyの根ryをxの根rxにつける
    }

    bool same(ll x,ll y){//xとyが属する木が同じかを返す
        ll rx=root(x);
        ll ry=root(y);
        return rx==ry;
    }

    ll size(ll x){ //素集合のサイズ
        return siz[root(x)];
    }
};

signed main(){
    ll n,k,l;cin >> n >> k >> l;

    UnionFind uf1(n);
    vector< pair<ll,ll> > pq(k);
    REP(i,k){cin >> pq[i].F >> pq[i].S;pq[i].F-=1;pq[i].S-=1;}
    sort(ALL(pq));
    REP(i,k){uf1.unite(pq[i].F,pq[i].S);}
    REP(i,n){uf1.root(i);}

    UnionFind uf2(n);
    vector< pair<ll,ll> > rs(l);
    REP(i,l){cin >> rs[i].F >> rs[i].S;rs[i].F-=1;rs[i].S-=1;}
    sort(ALL(rs));
    REP(i,l){uf2.unite(rs[i].F,rs[i].S);}
    REP(i,n){uf2.root(i);}

    REP(i,n){cout << uf1.parent[i] << endl;}
    REP(i,n){cout << uf2.parent[i] << endl;}
    
}