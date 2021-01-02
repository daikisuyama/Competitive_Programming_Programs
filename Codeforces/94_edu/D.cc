//デバッグ用オプション：-fsanitize=undefined,address

//コンパイラ最適化
#pragma GCC optimize("Ofast")

//インクルードなど
#include<bits/stdc++.h>
using namespace std;
typedef int ll;

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
#define MOD 4000 //10^9+7:合同式の法
#define MAXR 100000 //10^5:配列の最大のrange
//略記
#define PB push_back //挿入
#define MP make_pair //pairのコンストラクタ
#define F first //pairの一つ目の要素
#define S second //pairの二つ目の要素

//MLE

signed main(){
    //入力の高速化用のコード
    //ios::sync_with_stdio(false);
    //cin.tie(nullptr);
    ll t;cin>>t;
    REP(_,t){
        ll n;cin>>n;
        vector<ll> a(n);
        REP(i,n)cin>>a[i];
        //それぞれの値で管理
        map<ll,vector<ll>> m;
        REP(i,n){
            FOR(j,i+1,n-1){
                m[a[i]*MOD+a[j]].PB(i*MOD+j);
            }
        }
        long long ans=0;
        FORA(i,m){
            //二分探索
            ll m=SIZE(i.S);
            REP(j,m-1){
                ll l,r;l=j+1;r=m-1;
                if(i.S[j]%MOD<ll(i.S[l]/MOD)){
                    ans+=(m-j-1);
                    continue;
                }
                if(i.S[j]%MOD>=ll(i.S[r]/MOD)){
                    continue;
                }
                while(l+1<r){
                    ll k=l+(r-l)/2;
                    if(ll(i.S[k]/MOD)>i.S[j]%MOD){
                        r=k;
                    }else{
                        l=k;
                    }
                }
                ans+=(m-r);
            }
        }
        cout<<ans<<endl;
    }
}