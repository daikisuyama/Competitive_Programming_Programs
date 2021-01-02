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

vector<vector<ll>> tree;
vector<ll> cost;
bool check;

//インデックスと値の組で返す(値、index)
//全て異なるように！(かぶってる時の処理がめんどい)
//途中から+で関係性が崩れないように！
vector<pair<ll,ll>> dfs(ll v){
    vector<pair<ll,ll>> ret={};
    FORA(i,tree[v]){
        FORA(j,dfs(i)){
            ret.PB(j);
        }
    }
    sort(ALL(ret));
    //cout<<cost[v]<<SIZE(ret)<<endl;
    if(cost[v]>SIZE(ret)){
        check=true;
        return {};
    }else if(cost[v]==SIZE(ret)){
        if(SIZE(ret)==0){
            ret.PB(MP(1,v));
            return ret;
        }else{
            ret.PB(MP(ret[SIZE(ret)-1].F+1,v));
            return ret;
        }
    }else if(cost[v]==0){
        FOR(i,cost[v],SIZE(ret)-1){
            ret[i].F++;
        }
        ret.PB(MP(1,v));
        return ret;
    }else{
        ll x=ret[cost[v]].F;
        if(ret[cost[v]-1].F+1<ret[cost[v]].F){
            ret.PB(MP(x-1,v));
            return ret;
        }else{
            FOR(i,cost[v],SIZE(ret)-1){
                ret[i].F++;
                ret[i].F++;
            }
            ret.PB(MP(x+1,v));
            return ret;
        }
    }
}

signed main(){
    //入力の高速化用のコード
    //ios::sync_with_stdio(false);
    //cin.tie(nullptr);
    check=false;
    ll n;cin>>n;
    tree=vector<vector<ll>>(n);
    cost=vector<ll>(n);
    ll root;
    REP(i,n){
        ll p,c;cin>>p>>c;p--;
        if(p!=-1){
            tree[p].PB(i);
        }else{
            root=i;
        }
        cost[i]=c;
    }
    vector<pair<ll,ll>> d=dfs(root);
    vector<ll> ans(n);
    FORA(i,d){
        ans[i.S]=i.F;
    }
    if(check){
        cout<<"NO"<<endl;
        return 0;
    }
    cout<<"YES"<<endl;
    REP(i,n){
        if(i!=n-1)cout<<ans[i]<<" ";
        else cout<<ans[i]<<endl;
    }
}   