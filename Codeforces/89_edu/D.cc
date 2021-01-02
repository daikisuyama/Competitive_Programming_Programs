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
#define MAXR 10000000 //10^5:配列の最大のrange
//略記
#define PB push_back //挿入
#define MP make_pair //pairのコンストラクタ
#define F first //pairの一つ目の要素
#define S second //pairの二つ目の要素

//MAXR=10^5であることに注意
#define PN 1 //素数のマークは1

vector<ll> PN_chk(MAXR+1,PN);//0-indexed(0~MAXR)

//素因数分解に含まれる素数を保存するset
set<ll> prime;

//O(MAXR)
void init_eratosthenes(){
    ll MAXRR=sqrt(MAXR)+1;
    //2以上の数の素因数分解をするので無視して良い
    PN_chk[0]=0;PN_chk[1]=0;
    FOR(i,2,MAXRR){
        //たどり着いた時に素数と仮定されているなら素数
        //ある素数の倍数はその素数で割り切れるのでマークづけ
        if(PN_chk[i]==1) FOR(j,i,ll(MAXR/i)){PN_chk[j*i]=i;}
    }
}

//O(logn)
//mapなのでprimeは整列済
//二個しかいらぬ
void prime_factorize(ll n){
    if(n<=1) return;
    //if(SIZE(prime)==2)return;
    //1の場合はnは素数
    if(PN_chk[n]==1){prime.insert(n);return;}
    //マークされている数は素数
    prime.insert(PN_chk[n]);
    //マークされている数でnを割った数を考える
    prime_factorize(ll(n/PN_chk[n]));
}

signed main(){
    //入力の高速化用のコード
    //ios::sync_with_stdio(false);
    //cin.tie(nullptr);
    init_eratosthenes();
    ll n;cin>>n;
    vector<ll> a(n);REP(i,n)cin>>a[i];
    vector<ll> ans0(n,-1);
    vector<ll> ans1(n,-1);
    REP(i,n){
        if(a[i]%2==1){
            prime_factorize(a[i]);
            if(SIZE(prime)>1){
                ans0[i]=*prime.begin();
                ans1[i]=*++(prime.begin());
            }
            prime.clear();
        }else{
            prime_factorize(a[i]);
            if(SIZE(prime)>1){
                ans0[i]=2;ans1[i]=1;
                for(auto j=++prime.begin();j!=prime.end();j++){
                    ans1[i]*=(*j);
                }
            }
            prime.clear();
        }
    }
    REP(i,n){
        if(i==n-1)cout<<ans0[i]<<"\n";
        else cout<<ans0[i]<<" ";
    }
    REP(i,n){
        if(i==n-1)cout<<ans1[i]<<"\n";
        else cout<<ans1[i]<<" ";
    }
}