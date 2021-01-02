#include<iostream>
#include<vector>
#include<algorithm>
#include<utility>
using namespace std;
typedef long long ll;

//参考：https://pyteyon.hatenablog.com/entry/2019/03/11/200000
//参考：https://qiita.com/ofutonfuton/items/c17dfd33fc542c222396

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
    ll n,m;cin >> n >> m;
    vector< pair<ll,ll> > ab(m);
    for(ll i=m-1;i>=0;i--){cin >> ab[i].first >> ab[i].second;}
    UnionFind uf(n);
    vector<ll> ans(m);ans[0]=(n*(n-1))/2;//cout << ans[0] << endl;
    for(ll i=0;i<m-1;i++){
        //ここで更新も同時に起こってる
        ll a,b;a=ab[i].first-1;b=ab[i].second-1;
        if(uf.same(a,b)){
        ans[i+1]=ans[i];
        }else{
        ll sa,sb;sa=uf.size(a);sb=uf.size(b);
        ans[i+1]=ans[i]+(sa*(sa-1))/2+(sb*(sb-1))/2;
        uf.unite(a,b);sa=uf.size(a);
        ans[i+1]-=(sa*(sa-1))/2;
        }
    }
    for(ll i=m-1;i>=0;i--){
        cout << ans[i] << endl;
    }
}