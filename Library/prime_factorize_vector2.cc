//インクルード
#include<algorithm>//sort,二分探索,など
#include<bitset>//固定長bit集合
#include<cmath>//pow,logなど
#include<complex>//複素数
#include<deque>//両端アクセスのキュー
#include<functional>//sortのgreater
#include<iomanip>//setprecision(浮動小数点の出力の誤差)
#include<iostream>//入出力
#include<iterator>//集合演算(積集合,和集合,差集合など)
#include<map>//map(辞書)
#include<numeric>//iota(整数列の生成),gcdとlcm(c++17)
#include<queue>//キュー
#include<set>//集合
#include<stack>//スタック
#include<string>//文字列
#include<unordered_map>//イテレータあるけど順序保持しないmap
#include<unordered_set>//イテレータあるけど順序保持しないset
#include<utility>//pair
#include<vector>//可変長配列

using namespace std;
typedef long long ll;

//マクロ
#define REP(i,n) for(ll i=0;i<(ll)(n);i++)
#define REPD(i,n) for(ll i=(ll)(n)-1;i>=0;i--)
#define FOR(i,a,b) for(ll i=(a);i<=(b);i++)
#define FORD(i,a,b) for(ll i=(a);i>=(b);i--)
#define ALL(x) (x).begin(),(x).end() //sortなどの引数を省略したい
#define SIZE(x) ((ll)(x).size()) //sizeをsize_tからllに直しておく
#define MAX(x) *max_element(ALL(x))
#define INF 1000000000000 //10^12
#define MOD 10000007 //10^9+7
#define MAXR 100000 //10^5:配列の最大のrange(素数列挙などで使用)
#define PB push_back
#define MP make_pair
#define F first
#define S second

#define PN 1 //素数
#define MAXRR 1000 //√MAXR以上の数を設定する

//MAXRまでの整数は素数であると仮定する(ここから削る)
vector<ll> PN_chk(MAXR+1,PN);//0indexでi番目が整数iに対応(0~MAXR)

vector<ll> prime;//素因数分解して出てきた素数を全て挿入する

void se(){
    //0と1は素因数分解できない
    PN_chk[0]=0;PN_chk[1]=0;
    FOR(i,2,MAXRR){
        //たどり着いた時に素数と仮定されているなら素数
        if(PN_chk[i]==1) FOR(j,i,ll(MAXR/i)){PN_chk[j*i]=i;}
    }
}

void prime_factorize(ll n){
    if(n<=1) return;
    if(PN_chk[n]==1){prime.PB(n);return;}
    prime.PB(PN_chk[n]);
    prime_factorize(ll(n/PN_chk[n]));
}

signed main(){
    se();
    prime_factorize(5112);sort(ALL(prime));
    ll l=SIZE(prime);
    REP(i,l){
        if(i!=l-1) cout << prime[i] << " ";
        else cout << prime[i] << endl;
    }
}