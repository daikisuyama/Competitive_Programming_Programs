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

signed main(){
    //入力の高速化用のコード
    //ios::sync_with_stdio(false);
    //cin.tie(nullptr);
    ll n,m;cin>>n>>m;
    //準備できた日に対して
    vector<vector<pair<ll,ll>>> preparation(n);
    //試験日に対してのind
    vector<ll> ind(n,-1);
    REP(i,m){
        ll s,d,c;cin>>s>>d>>c;
        ind[d-1]=i;
        preparation[s-1].PB(MP(d-1,c));
    }
    vector<ll> ans(n,-1);
    set<pair<ll,ll>> cand;
    REP(i,n){
        REP(j,SIZE(preparation[i])){
            cand.insert(preparation[i][j]);
        }
        if(ind[i]!=-1){
            ans[i]=m+1;
            continue;
        }
        if(SIZE(cand)==0){
            ans[i]=0;
            continue;
        }
        auto j=cand.begin();
        if(j->F<i){
            cout<<-1<<endl;
            return 0;
        }
        ans[i]=ind[j->F]+1;
        pair<ll,ll> p=*j;p.S-=1;
        cand.erase(j);
        if(p.S!=0){
            cand.insert(p);
        }
    }
    if(SIZE(cand)==0){
        REP(i,n){
            if(i==n-1)cout<<ans[i]<<endl;
            else cout<<ans[i]<<" ";
        }
    }else{
        cout<<-1<<endl;
    }
}