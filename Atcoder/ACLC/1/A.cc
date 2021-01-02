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

    //コンストラクタ
    UnionFind(ll n):parent(n),siz(n,1){ 
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
    void grouping(ll n){
        //経路圧縮を先に行う
        REP(i,n)root(i);
        //mapで管理する(デフォルト構築を利用)
        REP(i,n)group[parent[i]].PB(i);
    }
};

signed main(){
    //入力の高速化用のコード
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    ll n;cin>>n;
    vector<ll> ind(n,0);
    vector<ll> checky(n,0);
    vector<ll> checkx(n,0);
    UnionFind uf(n);
    REP(i,n){
        ll x,y;cin>>x>>y;
        checky[x-1]=y-1;
        checkx[y-1]=x-1;
        ind[x-1]=i;
    }
    //checkyの中からそれより小さいものを探す(探す順番は値の順番)
    //checkyの値でsetを作っておいてその中で探す(終わったら削除)
    //値の順番なので、それ以降の省略ができる
    set<ll> set_checky;
    REP(i,n)set_checky.insert(i);
    REPD(i,n){
        //yの大きいところから探す(見つかったらbreak)
        //setないはxの順番
        auto j=set_checky.lower_bound(checkx[i]);
        if(j==set_checky.begin()){
            set_checky.erase(checkx[i]);
            continue;
        }
        //cout<<2<<endl;
        j--;
        while(true){
            //cout<<4<<endl;
            if(uf.same(ind[checkx[i]],ind[*j])){
                //cout<<4<<endl;
                if(ind[checkx[i]]!=ind[*j])break;
            }else{
                uf.unite(ind[checkx[i]],ind[*j]);
            }
            if(j==set_checky.begin())break;
            j--;
            //cout<<1<<endl;
        }
        /*
        REPD(j,checkx[i]){
            if(i>checky[j]){
                if(uf.same(ind[checkx[i]],ind[j])){
                    break;
                }else{
                    uf.unite(ind[checkx[i]],ind[j]);
                }
            }
        }
        */
        set_checky.erase(checkx[i]);
    }
    uf.grouping(n);
    REP(i,n){
        cout<<uf.size(i)<<endl;
    }
}