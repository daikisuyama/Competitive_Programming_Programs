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
#define CANT MP(ll(-1),ll(-1))

pair<ll,ll> dfs(vector<ll> &p,vector<ll> &h,vector<bool> &seen,vector<vector<ll>> &graph,ll v) {
    seen[v] = true;
    bool f=false;
    //良い悪いのペア
    pair<ll,ll> x(0,0);
    for (auto ne:graph[v]) { 
        if(seen[ne])continue;
        f=true;
        pair<ll,ll> y=dfs(p,h,seen,graph,ne);
        if(y==CANT)return CANT;
        x.F+=y.F;x.S+=y.S;
    }
    //cout<< x.F << " " << x.S << " " << v << endl;
    if(f){
        if(abs(p[v]+x.F+x.S)%2!=abs(h[v])%2){
            //cout<<-1<<endl;
            return CANT;
        }else{
            ll c=(p[v]+x.F+x.S+h[v])/2;ll d=(p[v]+x.F+x.S-h[v])/2;
            if(c<0 or d<0 or c<x.F){
                //cout<<-2<<endl;
                return CANT;
            }else{
                return MP(c,d);
            }
        }
    }else{
        if(abs(p[v]%2)!=abs(h[v]%2)){
            //cout<<-3<<endl;
            return CANT;
        }else{
            ll c=(p[v]+h[v])/2;ll d=(p[v]-h[v])/2;
            if(c<0 or d<0){
                //cout<<-4<<endl;
                return CANT;
            }else{
                return MP(c,d);
            }
        }
    }
}

signed main(){
    //入力の高速化用のコード
    //ios::sync_with_stdio(false);
    //cin.tie(nullptr);
    ll t;cin>>t;
    REP(_,t){
        ll n,m;cin>>n>>m;
        vector<bool> seen(n,false);
        vector<vector<ll>> graph(n);
        vector<ll> p(n);REP(i,n)cin>>p[i];
        vector<ll> h(n);REP(i,n)cin>>h[i];
        REP(i,n-1){
            ll x,y;cin>>x>>y;
            graph[x-1].PB(y-1);
            graph[y-1].PB(x-1);
        }
        pair<ll,ll> z=dfs(p,h,seen,graph,0);
        if(z==CANT){
            cout<<"NO"<<endl;
        }else{
            cout<<"YES"<<endl;
        }
    }
}