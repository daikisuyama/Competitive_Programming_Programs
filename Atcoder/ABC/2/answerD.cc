//OK
//あとで復習

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
#define FORALL(i,x) for(auto i=x.begin();i!=x.end();i++)
#define SIZE(x) ((ll)(x).size()) //sizeをsize_tからllに直しておく
#define MAX(x) *max_element(ALL(x))
#define INF 1000000000000
#define MOD 10000007
#define PB push_back
#define MP make_pair
#define F first
#define S second

//全員が知り合い
//全探索で多分間に合うはず
signed main(){
    ll n,m;cin >> n >> m;
    set< pair<ll,ll> > xy;
    REP(i,m){
        pair<ll,ll> xy_sub1,xy_sub2;
        cin >> xy_sub1.F >> xy_sub1.S;
        xy_sub1.F-=1;xy_sub1.S-=1;
        xy_sub2.F=xy_sub1.S;xy_sub2.S=xy_sub1.F;
        xy.insert(xy_sub1);
        xy.insert(xy_sub2);
    }
    ll ans=1;
    REP(i,pow(2,n)){
        vector<ll> vec;
        REP(j,n){
            if(i>>j&1)vec.PB(j);
        }
        ll le=vec.size();
        bool ce=false;
        //cout << endl;
        FORALL(j,vec){
            FORALL(k,vec){
                if(*j!=*k){
                    //cout << *j << " " << *k << endl;
                    pair<ll,ll> p=MP(*j,*k);
                    if(xy.find(p)==xy.end()){
                        ce=true;
                    }
                }
                if(ce)break;                
            }
            if(ce)break;   
        }
        if(!ce) ans=max(ans,le);
    }
    cout << ans << endl;
}