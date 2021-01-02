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
    ll n,k,x;cin>>n>>k>>x;
    vector<ll> a(n);REP(i,n)cin>>a[i];
    if(k==1){
        if(x!=n){
            cout<<-1<<endl;
        }else{
            cout<<accumulate(ALL(a),0LL)<<endl;
        }
        return 0;
    }
    //なぜか初期化が
    //ダメな場合は-1
    vector<vector<vector<ll>>> dp(n,vector<vector<ll>>(x+1,vector<ll>(n,-1)));
    //初期化(iを選ぶか)
    dp[0][1][0]=a[0];
    REP(i,k-1){
        //初めて選ぶ場合
        dp[i+1][1][i+1]=a[i+1];
        REP(j,x+1){
            REP(l,n){
                if(true){
                    if(dp[i][j][l]!=-1){
                        //選ぶ場合
                        if(j!=x){
                            dp[i+1][j+1][i+1]=max(dp[i+1][j+1][i+1],dp[i][j][l]+a[i+1]);
                        }
                        //選ばない場合
                        dp[i+1][j][l]=max(dp[i+1][j][l],dp[i][j][l]);
                    }
                }
            }
        }
    }
    //遷移
    FOR(i,k-1,n-2){
        REP(j,x+1){
            REP(l,n){
                if(true){
                    if(dp[i][j][l]!=-1){
                        //選ぶ場合
                        if(j!=x and (i+1)-l<=k){
                            dp[i+1][j+1][i+1]=max(dp[i+1][j+1][i+1],dp[i][j][l]+a[i+1]);
                        }
                        //選ばない場合
                        dp[i+1][j][l]=max(dp[i+1][j][l],dp[i][j][l]);
                    }
                }
            }
        }
    }
    //ここの範囲
    ll ans=-1;
    FOR(l,n-1-(k-1),n-1){
        ans=max(ans,dp[n-1][x][l]);
    }
    cout<<ans<<endl;
}