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
#define MOD 1000000007 //10^9+7:合同式の法
#define INF 1000000000000 //10^12
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
    ll n;cin>>n;
    vector<ll> h(n);REP(i,n)cin>>h[i];
    vector<ll> move1(n);
    vector<ll> move2(n);
    vector<vector<ll>> move3(n);
    vector<vector<ll>> move4(n);
    //単に右にいく場合以外も

    //まずはmin
    set<pair<ll,ll>> minm;
    minm.insert(MP(h[0],0));
    FOR(i,1,n-1){
        if(SIZE(minm)==0){
            minm.insert(MP(h[i],i));
            continue;
        }
        //upper_boundで隣は危険！！(一生バグらせた)
        auto x=minm.begin();
        while(x!=minm.end() and *x<=MP(h[i],n)){
            move1[x->S]=i;
            x=minm.erase(x);
        }
        minm.insert(MP(h[i],i));
    }

    //次にmax
    set<pair<ll,ll>> maxm;
    maxm.insert(MP(h[0],0));
    FOR(i,1,n-1){
        if(SIZE(maxm)==0){
            maxm.insert(MP(h[i],i));
            continue;
        }
        auto x=maxm.lower_bound(MP(h[i],0));
        while(x!=maxm.end()){
            move2[x->S]=i;
            x=maxm.erase(x);
        }
        maxm.insert(MP(h[i],i));
    }


    //逆からも(このパターン！)

    //まずはmin
    set<pair<ll,ll>> mint;
    mint.insert(MP(h[n-1],n-1));
    FORD(i,n-2,0){
        if(SIZE(mint)==0){
            mint.insert(MP(h[i],i));
            continue;
        }
        //upper_boundで隣は危険！！(一生バグらせた)
        auto x=mint.begin();
        while(x!=mint.end() and *x<=MP(h[i],n)){
            move3[i].PB(x->S);
            x=mint.erase(x);
        }
        mint.insert(MP(h[i],i));
    }
    //次にmax
    set<pair<ll,ll>> maxt;
    maxt.insert(MP(h[n-1],n-1));
    FORD(i,n-2,0){
        if(SIZE(maxt)==0){
            maxt.insert(MP(h[i],i));
            continue;
        }
        auto x=maxt.lower_bound(MP(h[i],0));
        while(x!=maxt.end()){
            move4[i].PB(x->S);
            x=maxt.erase(x);
        }
        maxt.insert(MP(h[i],i));
    }

    vector<ll> dp(n,INF);
    dp[0]=0;
    REP(i,n-1){
        dp[i+1]=min(dp[i+1],dp[i]+1);
        dp[move1[i]]=min(dp[move1[i]],dp[i]+1);
        dp[move2[i]]=min(dp[move2[i]],dp[i]+1);
        FORA(j,move3[i])dp[j]=min(dp[j],dp[i]+1);
        FORA(j,move4[i])dp[j]=min(dp[j],dp[i]+1);
    } 
    cout<<dp[n-1]<<endl;
}