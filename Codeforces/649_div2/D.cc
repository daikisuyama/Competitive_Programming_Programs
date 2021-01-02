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
class UnionFind {
public:
    vector<ll> parent; //parent[i]はiの親
    vector<ll> siz; //素集合のサイズを表す配列(1で初期化)
    map<ll,vector<ll>> group;//素集合ごとに管理する連想配列(keyはそれぞれの素集合の親、valueはその素集合の要素の配列)

    //コンストラクタの:の後ろでメンバ変数を初期化
    UnionFind(ll n):parent(n),siz(n,1){ 
        //最初は全ての要素の根はそれ自身であるとして初期化
        for(ll i=0;i<n;i++){parent[i]=i;}
    }

    ll root(ll x){ //データxの属する木の根を取得
        if(parent[x]==x) return x;

        return parent[x]=root(parent[x]);
        //代入式の値は代入した変数の値になる
        //経路圧縮(根に直接要素を繋ぐことで計算を効率化する)を行っている
    }

    void unite(ll x,ll y){ //xとyの木を併合
        ll rx=root(x);//xの根をrx
        ll ry=root(y);//yの根をry
        if(rx==ry) return; //同じ木にある時
        //小さい集合を大きい集合へと併合(ry→rxへ併合)
        if(siz[rx]<siz[ry]) swap(rx,ry);
        siz[rx]+=siz[ry];
        parent[ry]=rx; //xとyが同じ木にない時はyの根ryをxの根rxにつける
    }

    bool same(ll x,ll y){//xとyが属する木が同じかを判定
        ll rx=root(x);
        ll ry=root(y);
        return rx==ry;
    }

    ll size(ll x){ //xの素集合のサイズを取得
        return siz[root(x)];
    }

    //↓他の人のライブラリにはないけど便利だと思う関数
    //O(n)であることに注意
    void grouping(ll n){//素集合どうしをグループ化
        REP(i,n){
            if(group.find(parent[i])==group.end()){
                group[parent[i]]={i};
            }else{
                group[parent[i]].PB(i);
            }
        }
    }
};

signed main(){
    //入力の高速化用のコード
    //ios::sync_with_stdio(false);
    //cin.tie(nullptr);
    ll n,m,k;cin>>n>>m>>k;
    UnionFind uf(n);
    REP(_,m){
        ll u,v;cin>>u>>v;
        uf.unite(u-1,v-1);
    }
    uf.grouping(n);
    ll s=SIZE(uf.group);
    vector<ll> ans;
    if(s>=ll(k/2)){
        ll j=0;
        FORA(i,uf.group){
            ans.PB(i.S[0]);
            j++;
            if(j==ll(k/2))break;
        }
        cout<<1<<endl;
        REP(i,ll(k/2)){
            if(i==ll(k/2)-1)cout<<ans[i]<<endl;
            else cout<<ans[i]<<" ";
        }
    }else{
        
    }
}