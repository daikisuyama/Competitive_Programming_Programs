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

ll n,m;
vector<vector<ll>> edges;
vector<ll> dpc;
vector<vector<ll>> tree;
vector<ll> p;
vector<bool> check;

//部分木の頂点数
ll dfs(ll i){
    //cout<<1<<endl;
    ll ret=1;
    check[i]=true;
    FORA(j,tree[i]){
        if(!check[j]){
            ret+=dfs(j);
        }
    }
    dpc[i]=ret;
    return ret;
}

signed main(){
    //入力の高速化用のコード
    //ios::sync_with_stdio(false);
    //cin.tie(nullptr);
    //どうせオーバフロー
    ll t;cin>>t;
    REP(_,t){
        cin>>n;
        dpc=vector<ll>(n,0);
        tree=vector<vector<ll>>(n);
        edges=vector<vector<ll>>(n-1);
        check=vector<bool>(n,false);
        REP(i,n-1){
            ll u,v;cin>>u>>v;u--;v--;
            tree[u].PB(v);
            tree[v].PB(u);
            edges[i]={u,v};
        }
        dfs(0);
        vector<ll> dp(n-1,0);
        REP(i,n-1){
            ll l,r;l=edges[i][0];r=edges[i][1];
            dp[i]=min(dpc[l],dpc[r])*(n-min(dpc[l],dpc[r]));
        }
        //FORA(i,dpc)cout<<i<<" ";
        sort(ALL(dp),greater<ll>());
        //計算過程
        cin>>m;
        p=vector<ll>(m);
        REP(i,m){
            cin>>p[i];
        }
        sort(ALL(p),greater<ll>());
        vector<ll> calc(n-1,1);
        if(m<n-1){
            REP(i,m){
                calc[i]=p[i];
            }
        }else{
            //多分こっち側が違う
            //あとで直す
            REP(i,m-n+2){
                calc[0]*=p[i];
                calc[0]%=MOD;
            }
            FOR(i,m-n+2,m-1){
                calc[i-m+n-1]=p[i];
            }
        }
        ll ans=0;
        REP(i,n-1){
            ans+=(calc[i]*dp[i]);
            ans%=MOD;
        }
        cout<<ans<<endl;
    }
}