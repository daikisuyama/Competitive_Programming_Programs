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
    //小数の桁数の出力指定
    //cout<<fixed<<setprecision(10);
    //入力の高速化用のコード
    //ios::sync_with_stdio(false);
    //cin.tie(nullptr);
    ll t;cin>>t;
    REP(_,t){
        map<ll,vector<ll>> m;
        ll n;cin>>n;
        REP(i,n){
            ll a;cin>>a;
            m[a].PB(i);
        }
        vector<pair<ll,ll>> values;
        FORA(i,m){
            ll s=SIZE(i.S);
            ll mi=-1;
            REP(j,s){
                if(j==0){
                    mi=max(mi,i.S[j]+1);
                }
                if(j==s-1){
                    mi=max(mi,n-i.S[j]);
                }
                if(j!=s-1){
                    mi=max(mi,i.S[j+1]-i.S[j]);
                }
            }
            values.PB(MP(i.F,mi));
        }
        
        vector<ll> ans(n,-1);
        ll sv=SIZE(values);
        #if 0
        REP(i,sv){
            if(i==sv-1)cout<<values[i].F<<" "<<values[i].S<<"\n";
            else cout<<values[i].F<<" "<<values[i].S<<endl;
        }
        cout<<endl;
        #endif
        ll now=n;
        REP(i,sv){
            while(values[i].S<=now){
                ans[now-1]=values[i].F;
                now--;
            }
        }
        REP(i,n){
            if(i==n-1)cout<<ans[i]<<"\n";
            else cout<<ans[i]<<" ";
        }
    }
}