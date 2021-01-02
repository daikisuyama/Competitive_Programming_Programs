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
#define INF 1000000000000LL //10^12:∞
#define MOD 1000000007 //10^9+7:合同式の法
#define MAXR 100000 //10^5:配列の最大のrange
//略記
#define PB push_back //挿入
#define MP make_pair //pairのコンストラクタ
#define F first //pairの一つ目の要素
#define S second //pairの二つ目の要素

vector<vector<ll>> tree;
vector<pair<ll,ll>> cost;


pair<ll,vector<ll>> bfs(ll i){
    deque<ll> d;
    FORA(j,tree[i]){
        d.PB(j);
        cost[j]={1,i};
    }
    while(SIZE(d)){
        ll l=SIZE(d);
        REP(_,l){
            ll p=d.front();d.pop_front();
            FORA(j,tree[p]){
                if(cost[j].F==INF){
                    cost[j]=MP(cost[p].F+1,p);
                    d.PB(j);
                }
            }
        }
    }
    if(cost[i].F==INF)return MP(INF,vector<ll>());
    vector<ll> ans={};
    ll now=cost[i].S;
    while(true){
        ans.PB(now+1);
        now=cost[now].S;
        if(now==i){
            ans.PB(now+1);
            break;
        }
    }
    return MP(cost[i].F,ans);
}


signed main(){
    //入力の高速化用のコード
    //ios::sync_with_stdio(false);
    //cin.tie(nullptr);
    //有向グラフ
    ll n,m;cin>>n>>m;
    tree=vector<vector<ll>>(n);
    REP(i,m){
        ll a,b;cin>>a>>b;
        tree[a-1].PB(b-1);
    }
    vector<pair<ll,vector<ll>>> ans;
    REP(i,n){
        cost=vector<pair<ll,ll>>(n,MP(INF,-1));
        pair<ll,vector<ll>> p=bfs(i);
        if(p!=MP(INF,vector<ll>()))ans.PB(p);
    }
    sort(ALL(ans));
    if(SIZE(ans)){
        cout<<SIZE(ans[0].S)<<endl;
        REP(i,SIZE(ans[0].S))cout<<ans[0].S[i]<<endl;
    }else{
        cout<<-1<<endl;
    }
}