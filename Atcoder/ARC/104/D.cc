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
    //対称性を利用
    //O(N^4)を落とす
    ll n,k,mod;cin>>n>>k>>mod;
    if(n==1){
        cout<<k<<endl;
        return 0;
    }else if(n==2){
        cout<<k<<endl;
        cout<<k<<endl;
        return 0;
    }
    ll ran=k*n*(n+1)/2;
    vector<vector<ll>> dp(n,vector<ll>(ran+1,0));
    REP(j,k+1){
        dp[0][j]=1;
    }
    FOR(i,1,n-1){
        REP(j,k*i*(i+1)/2+1){
            ll ran2=min(k+1,(ran-j)/(i+1)+1);
            REP(l,ran2){
                dp[i][j+l*(i+1)]+=dp[i-1][j];
                if(dp[i][j+l*(i+1)]>=mod)dp[i][j+l*(i+1)]-=mod;
            }
        }
    }
    cout<<k*dp[n-2][0]%mod<<endl;
    FOR(i,2,n-1){
        ll ans=0;
        FOR(j,1,ran){
            ans+=(dp[i-2][j]*dp[n-i-1][j]);
            ans%=mod;
        }
        cout<<((k+1)*ans+k)%mod<<endl;
    }
    cout<<k*dp[n-2][0]%mod<<endl;
}