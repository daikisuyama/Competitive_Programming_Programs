//デバッグ用オプション：-fsani

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
    ll n;//要素の個数

    //コンストラクタ
    UnionFind(ll n_):parent(n_),siz(n_,1),n(n_){ 
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

    void clear(){
        for(ll i=0;i<n;i++){parent[i]=i;}
        siz=vector<ll>(n,1);
        group.clear();
    }
};

signed main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    ll n;cin>>n;
    set<ll> x;
    //値に対してのind
    map<ll,ll> ind;
    //indに対しての値
    vector<ll> val(n);
    REP(i,n){
        ll y;cin>>y;
        x.insert(y);
        val[i]=y;
    }
    sort(ALL(val));
    REP(i,n){
        ind[val[i]]=i;
    }
    vector<ll> v(1,0);
    pair<ll,vector<ll>> ans=MP(1,v);
    UnionFind uf(n);
    REP(i,31){
        uf.clear();
        FORA(j,val){
            if(x.find(j+(1LL<<i))!=x.end()){
                uf.unite(ind[j],ind[j+(1LL<<i)]);
            }
        }
        uf.grouping();
        for(auto j=uf.group.begin();j!=uf.group.end();j++){
            if(SIZE(j->S)>ans.F){
                //3は超えない
                //sortされてない(valは)はー？？？？？？？
                if(ans.F==1){
                    if(SIZE(j->S)==2){
                        vector<ll> w(2);
                        w={j->S[0],j->S[1]};
                        ans=MP(2,w);
                    }else{
                        cout<<3<<endl;
                        cout<<val[j->S[0]]<<" "<<val[j->S[1]]<<" "<<val[j->S[2]]<<endl;
                        return 0;
                    }
                }
                if(ans.F==2){
                    if(SIZE(j->S)>2){
                        cout<<3<<endl;
                        cout<<val[j->S[0]]<<" "<<val[j->S[1]]<<" "<<val[j->S[2]]<<endl;
                        return 0;
                    }
                }
            }
        }
    }
    cout<<ans.F<<endl;
    REP(i,ans.F){
        if(i==ans.F-1){
            cout<<val[ans.S[i]]<<endl;
        }else{
            cout<<val[ans.S[i]]<<" ";
        }
    }
}