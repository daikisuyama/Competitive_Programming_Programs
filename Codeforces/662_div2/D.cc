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


//vectorの代わりにpair
//vectorを毎回生成しない
signed main(){
    //入力の高速化用のコード
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    ll ans=0;
    ll n,m;cin>>n>>m;
    vector<string> x(n);REP(i,n)cin>>x[i];
    vector<char> alph(26);alph[0]='a';
    for(ll i=1;i<26;i++){
        alph[i]=alph[i-1];
        alph[i]++;
    }
    vector<vector<ll>> y(n,vector<ll>(m,0));
    vector<vector<bool>> check(n,vector<bool>(m,true));
    FORA(i,alph){
        REP(j,n)REP(k,m)y[j][k]=(x[j][k]==i);
        REP(j,n)REP(k,m)check[j][k]=(x[j][k]!=i);
        ll d=2;
        deque<pair<ll,ll>> b;
        REP(j,n){
            REP(k,m){
                if(j==0 or j==n-1 or k==0 or k==m-1){
                    if(y[j][k]){
                        check[j][k]=true;
                        b.PB(MP(j,k));
                    }
                }else if(!(y[j-1][k] and y[j+1][k] and y[j][k-1] and y[j][k+1])){
                    if(y[j][k]){
                        check[j][k]=true;
                        b.PB(MP(j,k));
                    }
                }
            }
        }
        while(SIZE(b)){
            ll l=SIZE(b);
            REP(_,l){
                pair<ll,ll> c=*(b.begin());b.pop_front();
                if(c.F>0){
                    if(! check[c.F-1][c.S]){
                        check[c.F-1][c.S]=true;
                        y[c.F-1][c.S]=d;
                        b.PB(MP(c.F-1,c.S));
                    }
                }
                if(c.F<n-1){
                    if(! check[c.F+1][c.S]){
                        check[c.F+1][c.S]=true;
                        y[c.F+1][c.S]=d;
                        b.PB(MP(c.F+1,c.S));
                    }
                }
                if(c.S>0){
                    if(! check[c.F][c.S-1]){
                        check[c.F][c.S-1]=true;
                        y[c.F][c.S-1]=d;
                        b.PB(MP(c.F,c.S-1));
                    }
                }
                if(c.S<m-1){
                    if(! check[c.F][c.S+1]){
                        check[c.F][c.S+1]=true;
                        y[c.F][c.S+1]=d;
                        b.PB(MP(c.F,c.S+1));
                    }
                }
            }
            d+=1;
        }

        REP(j,n)REP(k,m)ans+=y[j][k];
    }
    cout<<ans<<endl;
}