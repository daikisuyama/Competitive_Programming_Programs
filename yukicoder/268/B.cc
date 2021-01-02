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

vector<ll> divisors;//約数を格納する配列

void make_divisors(ll n){
    FOR(i,1,sqrt(n)){
        if(n%i==0){
            divisors.PB(i);
            if(i!=n/i){
                divisors.PB(n/i);
            }
        }
    }
    sort(ALL(divisors),greater<ll>());
}

signed main(){
    //入力の高速化用のコード
    //ios::sync_with_stdio(false);
    //cin.tie(nullptr);
    ll t;cin>>t;
    REP(i,t){
        ll a,b;cin>>a>>b;
        divisors.clear();
        make_divisors(a);
        vector<ll> ans={};
        ll x=b-a;
        REP(i,SIZE(divisors)){
            ll z=x/divisors[i];
            REP(j,z)ans.PB(divisors[i]);
            x-=(z*divisors[i]);
            if(x==0)break;
        }
        cout<<SIZE(ans)<<endl;
        REP(i,SIZE(ans)){
            if(i==SIZE(ans)-1)cout<<ans[i]<<"\n";
            else cout<<ans[i]<<" ";
        }
    }
}