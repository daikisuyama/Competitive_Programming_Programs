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
    ll R,G,B;cin>>R>>G>>B;
    vector<ll> r(R);REP(i,R)cin>>r[i];sort(ALL(r),greater<ll>());
    vector<ll> g(G);REP(i,G)cin>>g[i];sort(ALL(g),greater<ll>());
    vector<ll> b(B);REP(i,B)cin>>b[i];sort(ALL(b),greater<ll>());
    vector<vector<vector<ll>>> dp(R+1,vector<vector<ll>>(G+1,vector<ll>(B+1,0)));
    REP(i,R+1){
        REP(j,G+1){
            REP(k,B+1){
                //pairごとで選ぶ、配るDP
                //思いつければ楽だけど
                //dp[i][j][k]:=i番目j番目k番目まで組にした時の
                bool f=false;
                if(i<R and j<G){
                    dp[i+1][j+1][k]=max(dp[i+1][j+1][k],dp[i][j][k]+r[i]*g[j]);
                    f=true;
                }
                if(i<R and k<B){
                    dp[i+1][j][k+1]=max(dp[i+1][j][k+1],dp[i][j][k]+r[i]*b[k]);
                    f=true;
                }
                if(j<G and k<B){
                    dp[i][j+1][k+1]=max(dp[i][j+1][k+1],dp[i][j][k]+g[j]*b[k]);
                    f=true;
                }
                if(!f){
                    if(i<R)dp[i+1][j][k]=max(dp[i+1][j][k],dp[i][j][k]);
                    if(j<G)dp[i][j+1][k]=max(dp[i][j+1][k],dp[i][j][k]);
                    if(k<B)dp[i][j][k+1]=max(dp[i][j][k+1],dp[i][j][k]);
                }
            }
        }
    }
    cout<<dp[R][G][B]<<endl;
}