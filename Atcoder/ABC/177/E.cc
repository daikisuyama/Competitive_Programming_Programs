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
#define MAXR 1000000 //10^6:配列の最大のrange
//略記
#define PB push_back //挿入
#define MP make_pair //pairのコンストラクタ
#define F first //pairの一つ目の要素
#define S second //pairの二つ目の要素

#define PN 1 //素数のマークは1

//MAXR(=10^6)までの整数が素数であると仮定する
vector<ll> PN_chk(MAXR+1,PN);//0indexでi番目が整数iに対応(0~MAXR)


//O(MAXR)
void se(){
    ll MAXRR=sqrt(MAXR)+1;
    //2以上の数の素因数分解をするので無視して良い
    PN_chk[0]=0;PN_chk[1]=0;
    FOR(i,2,MAXRR){
        //たどり着いた時に素数と仮定されているなら素数
        //ある素数の倍数はその素数で割り切れるのでマークづけ
        if(PN_chk[i]==1) FOR(j,i,ll(MAXR/i)){PN_chk[j*i]=i;}
    }
}

vector<ll> check(MAXR+1,0);

//O(logn)
//primeはこの場合は整列されてないので注意！！！
//一回のみのcheck
map<ll,ll> prime;

void prime_factorize(ll n){
    if(n<=1) return;
    //1の場合はnは素数
    if(PN_chk[n]==1){prime[n]+=1;return;}
    //マークされている数は素数
    prime[PN_chk[n]]+=1;
    //マークされている数でnを割った数を考える
    prime_factorize(ll(n/PN_chk[n]));
}

signed main(){
    se();
    //入力の高速化用のコード
    //ios::sync_with_stdio(false);
    //cin.tie(nullptr);
    ll n;cin>>n;
    vector<ll> a(n);REP(i,n)cin>>a[i];
    //check二回つくか
    REP(i,n){
        prime_factorize(a[i]);
        FORA(j,prime){
            check[j.F]++;
        }
        prime.clear();
    }
    ll g=gcd(a[0],a[1]);
    FOR(i,2,n-1){
        g=gcd(g,a[i]);
    }
    REP(i,MAXR+1){
        if(check[i]>=2){
            if(g==1){
                cout<<"setwise coprime"<<endl;
            }else{
                cout<<"not coprime"<<endl;
            }
            return 0;
        }
    }
    cout<<"pairwise coprime"<<endl;
}
