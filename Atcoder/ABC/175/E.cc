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
    ll r,c,k;cin>>r>>c>>k;
    vector<vector<ll>> item(r,vector<ll>(c,0));
    REP(i,k){
        ll x,y,z;cin>>x>>y>>z;
        item[x-1][y-1]=z;
    }
    vector<vector<vector<ll>>> dp(r,vector<vector<ll>>(c,vector<ll>(4,0)));
    if(item[0][0]>0)dp[0][0][1]=item[0][0];
    REP(i,r){
        REP(j,c){
            REP(l,4){
                if(l<3){
                    if(i!=r-1){
                        dp[i+1][j][0]=max(dp[i+1][j][0],dp[i][j][l]);
                        if(item[i+1][j]>0)dp[i+1][j][1]=max(dp[i+1][j][0],dp[i][j][l])+item[i+1][j];
                    }
                    if(j!=c-1){
                        dp[i][j+1][l]=max(dp[i][j+1][l],dp[i][j][l]);
                        if(item[i][j+1]>0)dp[i][j+1][l+1]=max(dp[i][j+1][l+1],dp[i][j][l]+item[i][j+1]);
                    }
                }else{
                    if(i!=r-1){
                        dp[i+1][j][0]=max(dp[i+1][j][0],dp[i][j][l]);
                        if(item[i+1][j]>0)dp[i+1][j][1]=max(dp[i+1][j][0],dp[i][j][l])+item[i+1][j];
                    }
                    if(j!=c-1){
                        dp[i][j+1][l]=max(dp[i][j+1][l],dp[i][j][l]);
                    }
                }
            }
        }
    }
    cout<<*max_element(ALL(dp[r-1][c-1]))<<endl;
}