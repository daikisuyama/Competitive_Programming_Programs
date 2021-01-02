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
#define INF 1000000000000000 //10^12:∞
#define MOD 1000000007 //10^9+7:合同式の法
#define MAXR 100000 //10^5:配列の最大のrange
//略記
#define PB push_back //挿入
#define MP make_pair //pairのコンストラクタ
#define F first //pairの一つ目の要素
#define S second //pairの二つ目の要素

vector<ll> a,b,c;
vector<vector<ll>> tree;
vector<bool> check;
vector<ll> ans;

void dfs1(ll i,ll m){
    FORA(j,tree[i]){
        if(!check[j]){
            check[j]=true;
            a[j]=min(a[j],m);
            dfs1(j,a[j]);
        }
    }
}

pair<ll,ll> dfs2(ll i){
    ll ret=0;
    pair<ll,ll> now={(b[i]==0 and c[i]==1),(b[i]==1 and c[i]==0)};
    FORA(j,tree[i]){
        if(!check[j]){
            check[j]=true;
            pair<ll,ll> d=dfs2(j);
            ret+=ans[j];
            now.F+=d.F;
            now.S+=d.S;
        }
    }
    ret+=(min(now.F,now.S)*a[i]*2);
    ans[i]=ret;
    return MP(now.F-min(now.F,now.S),now.S-min(now.F,now.S));
}

signed main(){
    //入力の高速化用のコード
    //ios::sync_with_stdio(false);
    //cin.tie(nullptr);
    ll n;cin>>n;
    a=vector<ll>(n);b=vector<ll>(n);c=vector<ll>(n);
    REP(i,n)cin>>a[i]>>b[i]>>c[i];
    tree=vector<vector<ll>>(n);
    REP(i,n-1){ll u,v;cin>>u>>v;tree[u-1].PB(v-1);tree[v-1].PB(u-1);}
    if(accumulate(ALL(b),0)!=accumulate(ALL(c),0)){cout<<-1<<endl;return 0;}
    check=vector<bool>(n,false);check[0]=true;
    dfs1(0,a[0]);
    ans=vector<ll>(n,INF);
    check=vector<bool>(n,false);check[0]=true;
    dfs2(0);
    cout<<ans[0]<<endl;
}