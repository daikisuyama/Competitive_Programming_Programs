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
#define MAXR 6000000 //10^5:配列の最大のrange
//略記
#define PB push_back //挿入
#define MP make_pair //pairのコンストラクタ
#define F first //pairの一つ目の要素
#define S second //pairの二つ目の要素

#define PN true //素数
#define NPN false //素数ではない
//非本質
#define MAXRR 3000 //√MAXR以上の数を設定する

//MAXRまでの整数は素数であると仮定する(ここから削る)
vector<bool> PN_chk(MAXR+1,PN);//0indexでi番目が整数iに対応(0~MAXR)
//素数を格納する配列を用意しておく
vector<ll> PNs;

void se(){
    //0と1は素数ではない
    PN_chk[0]=NPN;PN_chk[1]=NPN;

    FOR(i,2,MAXRR){
        //たどり着いた時に素数と仮定されているなら素数
        if(PN_chk[i]) FOR(j,i,ll(MAXR/i)){PN_chk[j*i]=NPN;}
    }
    FOR(i,2,MAXR){
        if(PN_chk[i]) PNs.PB(i);
    }
}

ll modpow(ll a,ll n,ll p){
    if(n==0)return 1;
    ll t=modpow(a,n/2,p);
    t=t*t%p;
    if(n&1)t=t*a%p;
    return t;
}

signed main(){
    //入力の高速化用のコード
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    se();
    ll t;cin>>t;
    REP(_,t){
        ll a,p;cin>>a>>p;
        if(!PN_chk[p]){
            cout<<-1<<endl;
            continue;
        }
        if(a%p==0){
            cout<<0<<endl;
            continue;
        }
        cout<<1<<endl;
    }
}