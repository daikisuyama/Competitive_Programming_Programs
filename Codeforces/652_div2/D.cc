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
    ll n=2000000;
    vector<vector<ll>> dp(n,vector<ll>(3,0));
    dp[0][0]=1;
    FOR(i,1,n-1){
        dp[i][0]+=dp[i-1][0];
        dp[i][1]+=dp[i-1][0];
        dp[i][0]+=dp[i-1][1]*2;
        dp[i][2]+=dp[i-1][1];
        dp[i][2]+=dp[i-1][2];
        dp[i][0]%=MOD;
        dp[i][1]%=MOD;
        dp[i][2]%=MOD;
    }
    vector<ll> ans(n,0);
    REP(i,3){
        if(i!=0){
            ans[i]+=(MOD+dp[i][2]-dp[i-1][2])*4;
            ans[i]%=MOD;
        }
        for(ll j=i;j<n-3;j+=3){
            ans[j+3]+=ans[j];
            ans[j+3]+=(MOD+dp[j+3][2]-dp[j+2][2])*4;
            ans[j+3]%=MOD;
        }
    }
    ll t;cin>>t;
    REP(i,t){
        cin>>n;
        cout<<ans[n-1]<<endl;
    }
}