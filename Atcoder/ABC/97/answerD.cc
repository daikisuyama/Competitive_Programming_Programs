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
#include<iterator>//set_intersection,set_union,set_differenceのため

using namespace std;
typedef long long ll;

//マクロ
#define REP(i,n) for(ll i=0;i<(ll)(n);i++)
#define REPD(i,n) for(ll i=(ll)(n)-1;i>=0;i--)
#define FOR(i,a,b) for(ll i=(a);i<=(b);i++)
#define FORD(i,a,b) for(ll i=(a);i>=(b);i--)
#define ALL(x) (x).begin(),(x).end() //sortなどの引数を省略したい
#define SIZE(x) ((ll)(x).size()) //sizeをsize_tからllに直しておく
#define MAX(x) *max_element(ALL(x))
#define INF 1000000000000 //10^12
#define MOD 10000007 //10^9+7
#define PB push_back
#define MP make_pair
#define F first
#define S second
#define MAXR 100000 //10^5:最大のrange(素数列挙などで使用)

//参考：https://pyteyon.hatenablog.com/entry/2019/03/11/200000
//参考：https://qiita.com/ofutonfuton/items/c17dfd33fc542c222396

class UnionFind {
public:
    vector<ll> parent; //parent[i]はiの親
    vector<ll> siz; //素集合のサイズを表す配列(1で初期化)
    map<ll,vector<ll>> group;

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

    void grouping(ll n){ //素集合どうしのグループ化
        for(ll i=0;i<n;i++){
            if(group.find(parent[i])==group.end()){
                group[parent[i]]=vector<ll>(1,i);
            }else{
                group[parent[i]].push_back(i);
            }
        }
    }
};


signed main(){
    ll n,m;cin >> n >> m;
    UnionFind uf(n);
    vector<ll> p(n);REP(i,n){cin >> p[i];p[i]-=1;}
    REP(i,m){
        ll x,y;cin>>x>>y;
        uf.unite(x-1,y-1);
    }
    REP(i,n)uf.root(i);
    uf.grouping(n);
    ll ans=0;
    for(auto j=uf.group.begin();j!=uf.group.end();j++){
        vector<ll> value=j->S;
        //REP(i,value.size()) cout << value[i] << " ";
        vector<ll> vecinter;
        vector<ll> value2;REP(i,value.size()) value2.PB(p[value[i]]);
        sort(ALL(value));sort(ALL(value2));
        //sortを忘れないように
        set_intersection(ALL(value),ALL(value2),back_inserter(vecinter));
        //cout << ans << endl;
        ans+=vecinter.size();
        //cout << endl;
    }
    cout << ans << endl;
}