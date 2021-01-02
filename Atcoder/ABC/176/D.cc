//不等号連続だめ

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

vector<vector<ll>> dp;
ll h,w;

void bfs(ll i,ll j){
    //cout<<1<<endl;
    ll zs=0;
    FOR(k,-1,1){
        FOR(l,-1,1){
            //cout<<1<<endl;
            if(0<=i+k and i+k<h and 0<=j+l and j+l<w and k*l==0){
                if(dp[i+k][j+l]!=-1){
                    if(dp[i+k][j+l]>dp[i][j]){
                        dp[i+k][j+l]=dp[i][j];
                        bfs(i+k,j+l);
                    }
                }else{
                    zs++;
                }
            }else{
                zs++;
            }
        }
    }
    if(zs!=8)return;
    //cout<<1<<endl;
    vector<ll> check(2);check[0]=-2;check[1]=2;
    REP(o,2){
        FOR(p,-2,2){
            ll k,l;k=check[o];l=p;
            if(0<=i+k and i+k<h and 0<=j+l and j+l<w){
                if(dp[i+k][j+l]!=-1){
                    if(dp[i+k][j+l]>dp[i][j]+1){
                        dp[i+k][j+l]=dp[i][j]+1;
                        bfs(i+k,j+l);
                    }
                }
            }
        }
    }
    REP(o,2){
        FOR(p,-2,2){
            ll k,l;k=p;l=check[o];
            if(0<=i+k and i+k<h and 0<=j+l and j+l<w){
                if(dp[i+k][j+l]!=-1){
                    if(dp[i+k][j+l]>dp[i][j]+1){
                        dp[i+k][j+l]=dp[i][j]+1;
                        bfs(i+k,j+l);
                    }
                }
            }
        }
    }
}

signed main(){
    //入力の高速化用のコード
    //ios::sync_with_stdio(false);
    //cin.tie(nullptr);
    cin>>h>>w;
    vector<ll> c(2);REP(i,2)cin>>c[i];
    vector<ll> d(2);REP(i,2)cin>>d[i];
    vector<string> s(h);REP(i,h)cin>>s[i];
    dp.resize(h);
    REP(i,h)dp[i].resize(w);
    REP(i,h)REP(j,w){
        if(s[i][j]=='#')dp[i][j]=-1;
        else dp[i][j]=INF;
    }
    //cout<<1<<endl;
    dp[c[0]-1][c[1]-1]=0;
    bfs(c[0]-1,c[1]-1);
    if(dp[d[0]-1][d[1]-1]!=INF)cout<<dp[d[0]-1][d[1]-1]<<endl;
    else cout<<-1<<endl;
}