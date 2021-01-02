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
#define MOD 1000000007 //10^9+7:合同式の法
#define MAXR 100000 //10^5:配列の最大のrange
//略記
#define PB push_back //挿入
#define MP make_pair //pairのコンストラクタ
#define F first //pairの一つ目の要素
#define S second //pairの二つ目の要素


ll check_divisors(ll x,ll y){
    ll ret=0;
    ll n=x-y;
    vector<ll> divisors;//約数を格納する配列
    FOR(i,1,sqrt(n)){
        if(n%i==0){
            divisors.PB(i);
            if(i!=n/i){
                divisors.PB(n/i);
            }
        }
    }
    //a-1の候補
    FORA(i,divisors){
        ll a,b,c;a=i+1;
        ll v,w;v=n/(a-1);w=(x+y)/(a+1);
        b=(v+w)/2;c=(w-v)/2;
        if(b>0 and c>0 and (a-1)*(b-c)==(x-y) and (a+1)*(b+c)==(x+y)){
            ret++;        
        }
    }
    return ret;
}

ll check_divisors2(ll x,ll y){
    ll ret=x-1;
    FOR(i,3,sqrt(x)){
        if(x%i==0){
            if(i!=ll(x/i)){
                ret+=2;
            }else{
                ret++;
            }
        }
    }
    if(x%2==0){
        if(2!=ll(x/2) and x!=2){
            ret++;
        }
    }
    if(x!=1 and x!=2)ret++;
    return ret;
}

signed main(){
    //入力の高速化用のコード
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    ll s;cin>>s;
    REP(i,s){
        ll x,y;cin>>x>>y;
        if(x<y)swap(x,y);
        if(x==y){
            cout<<check_divisors2(x,y)<<endl;
        }else{
            cout<<check_divisors(x,y)<<endl;
        }
    }
}