//Codeforcesで128bit整数を使いたいとき
//→__int128_tを使う&GNU C++17 (64)で提出する
//デバッグ用オプション：-fsanitize=undefined,address

//コンパイラ最適化
#pragma GCC optimize("Ofast")

//インクルードなど
#include<bits/stdc++.h>
using namespace std;
typedef long long ll;

//イテレーション
#define REP(i,n) for(ll i=0;i<ll(n);i++)
#define REPD(i,n) for(ll i=n-1;i>=0;i--)
#define FOR(i,a,b) for(ll i=a;i<=ll(b);i++)
#define FORD(i,a,b) for(ll i=a;i>=ll(b);i--)
#define FORA(i,I) for(const auto& i:I)
//x:コンテナ
#define ALL(x) x.begin(),x.end() 
#define SIZE(x) ll(x.size()) 
//定数
#define INF32 2147483647 //2.147483647×10^{9}:32bit整数のinf
#define INF64 9223372036854775807 //9.223372036854775807×10^{18}:64bit整数のinf
#define MOD 1000000007 //問題による
#define MAXR 1000000 //10^6:前計算の配列の範囲
//略記
#define PB push_back 
#define MP make_pair
#define F first
#define S second

//aをbで割る時の繰上げ,繰り下げ
ll myceil(ll a,ll b){return (a+(b-1))/b;}
ll myfloor(ll a,ll b){return a/b;}


//割り切れる数でマーク
vector<ll> PNch;

//O(n log{log{n}})
void ES(ll n){
    //素数として初期化
    PNch.assign(n+1,1);
    //素因数分解は2以上で可能とする
    PNch[0]=0;PNch[1]=0;
    ll l=sqrt(n);
    FOR(i,2,l){
        //ある素数の倍数ならばその素数で割り切れる
        if(PNch[i]==1){
            FOR(j,i,n/i)PNch[j*i]=i;
        }
    }
}

//O(log{n})
class PFvec{
public:
    //PNs:=(素因数分解出てくる素数を昇順に格納したvector)
    vector<ll> PNs;
    PFvec(ll n){PF(n);}
    void PF(ll n){
        if(n<=1) return;
        //nが素数の時
        if(PNch[n]==1){PNs.PB(n);return;}
        //マークされている数は素数
        PNs.PB(PNch[n]);
        //マークされている数でnを割った数
        PF(n/PNch[n]);
    }
};

class PFmap{
public:
    //PNs:=(素因数分解出てくる素数を(昇順に)格納したmap)
    map<ll,ll> PNs;
    PFmap(ll n){PF(n);}
    void PF(ll n){
        if(n<=1) return;
        //nが素数の時
        if(PNch[n]==1){PNs[n]++;return;}
        //マークされている数は素数
        PNs[PNch[n]]++;
        //マークされている数でnを割った数
        PF(n/PNch[n]);
    }
};


signed main(){
    //小数の桁数の出力指定
    //cout<<fixed<<setprecision(10);
    //入力の高速化用のコード
    //ios::sync_with_stdio(false);
    //cin.tie(nullptr);
    //11/28 16:47~
    ll MR=1000000;
    ES(MR);
    vector<ll> p(MR+1,0);
    REP(i,MR+1){
        if(i%2==0)continue;
        if(PNch[i]==1 and PNch[(i+1)/2]==1)p[i]=1;
    }
    REP(i,MR){
        p[i+1]+=p[i];
    }
    ll q;cin>>q;
    REP(i,q){
        ll l,r;cin>>l>>r;
        cout<<p[r]-p[l-1]<<endl;
    }   
}