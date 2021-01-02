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
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    ll n;cin>>n;
    vector<bool> check(100001,false);
    vector<ll> a;
    REP(i,n){
        ll x;cin>>x;
        check[x]=true;
    }
    FOR(i,1,100000){
        if(check[i])a.PB(i);
    }
    n=SIZE(a);
    if(n==1){
        cout<<a[0]<<endl;
        return 0;
    }
    //大きい方から順に探していく(とりあえず最大のもので)
    ll ans=lcm(a[n-1],a[n-2]);
    //a[i]とのgcd、ただしans/a[i]より大きいものかつa[i]より小さいものを探す
    auto la=a.end();
    REPD(i,n){
        for(auto j=upper_bound(a.begin(),la,ans/a[i]);j!=a.end();j++){
            if(*j>=a[i] or (*j)*a[i]<ans)break;
            ans=max(ans,lcm(a[i],*j));
        }
        la--;
    }
    cout<<ans<<endl;
}