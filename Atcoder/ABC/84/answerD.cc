//エラトステネスの篩バグってんのクソすぎ(素数の整理)
//参考：http://ehafib.hatenablog.com/entry/2015/12/23/164517
//インクルード
#include<algorithm>//sort,二分探索,など
#include<bitset>//固定長bit集合
#include<cmath>//pow,logなど
#include<complex>//複素数
#include<deque>//両端アクセスのキュー
#include<functional>//sortのgreater
#include<iomanip>//setprecision(浮動小数点の出力の誤差)
#include<iostream>//入出力
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
#define INF 1000000000000
#define MOD 10000007
#define MA 100000
#define PB push_back
#define MP make_pair
#define F first
#define S second


ll sieve_check[MA+1];//i番目が整数iに対応(1~100000)

//エラトステネスの篩を実装する
void es(){
    FOR(i,2,MA)sieve_check[i]=1;
    //1のところが素数、ここでは0が素数でない
    for(ll i=2;i<=1000;i++){
        if(sieve_check[i]==1){
            for(ll j=2;j<=ll(MA/i);j++){
                sieve_check[j*i]=0;
            }
        }
    }
}

signed main(){
    es();
    vector<ll> pre(MA+1);FOR(i,1,MA)pre[i]=(i%2==1&&sieve_check[i]&&sieve_check[(i+1)/2]);
    REP(i,MA)pre[i+1]+=pre[i];
    ll q;cin >> q;
    vector< pair<ll,ll> > ans(q);REP(i,q) cin >> ans[i].F >> ans[i].S;
    REP(i,q)cout << pre[ans[i].S]-pre[ans[i].F-1] << endl;
}