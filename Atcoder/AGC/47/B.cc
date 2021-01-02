//デバッグ用オプション：-fsanitize=undefined,address

//コンパイラ最適化
#pragma GCC optimize("Ofast")

//インクルードなど
#include<bits/stdc++.h>
using namespace std;
typedef unsigned int ll;
typedef map<string,ll> map_type;

//マクロ
#define REP(i,n) for(ll i=0;i<ll(n);i++)
#define REPD(i,n) for(ll i=n-1;i>=0;i--)
#define FOR(i,a,b) for(ll i=a;i<=ll(b);i++)
#define FORD(i,a,b) for(ll i=a;i>=ll(b);i--)
#define FORA(i,I) for(const auto& i:I)
//xにはvectorなどのコンテナ
#define ALL(x) x.begin(),x.end() 
#define SIZE(x) ll(x.size()) 

inline ll chi(char x){
    return ll(x-'a');
}

signed main(){
    //入力の高速化用のコード
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    ll n;cin>>n;
    vector<string> ss(n);
    REP(i,n)cin>>ss[i];
    vector<map_type> m(1000000);
    vector<vector<ll>> check(n);
    REP(i,n){
        ll l=SIZE(ss[i]);
        check[i].resize(l);
        check[i][0]=1<<chi(ss[i][0]);
        FOR(j,1,l-1){
            check[i][j]=check[i][j-1]|(1<<chi(ss[i][j]));
        }
    }
    REP(i,n){
        //長さで分けてみる
        ll l=SIZE(ss[i]);
        m[l-1][ss[i].substr(1)]|=1<<chi(ss[i][0]);
    }
    ll ans=0;
    REP(i,n){
        ll l=SIZE(ss[i]);
        if(l==1)continue;
        string s="";
        ll now=0;
        ans+=__builtin_popcount(m[now][s]&check[i][l-1]);
        FORD(j,l-1,2){
            s=ss[i][j]+s;
            now++;
            //builtinpopcountにする
            if(m[now].find(s)!=m[now].end()){
                ans+=__builtin_popcount(m[now][s]&check[i][j-1]);
            }
        }
    }
    cout<<ans<<endl;
}
