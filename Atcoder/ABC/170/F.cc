//インクルード(アルファベット順)
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
//forループ関係
//引数は、(ループ内変数,動く範囲)か(ループ内変数,始めの数,終わりの数)、のどちらか
//Dがついてないものはループ変数は1ずつインクリメントされ、Dがついてるものはループ変数は1ずつデクリメントされる
#define REP(i,n) for(ll i=0;i<(ll)(n);i++)
#define REPD(i,n) for(ll i=n-1;i>=0;i--)
#define FOR(i,a,b) for(ll i=a;i<=(ll)(b);i++)
#define FORD(i,a,b) for(ll i=a;i>=(ll)(b);i--)
//xにはvectorなどのコンテナ
#define ALL(x) (x).begin(),(x).end() //sortなどの引数を省略したい
#define SIZE(x) ((ll)(x).size()) //sizeをsize_tからllに直しておく
#define MAX(x) *max_element(ALL(x)) //最大値を求める
#define MIN(x) *min_element(ALL(x)) //最小値を求める
//定数
#define INF 1000000000000 //10^12:極めて大きい値,∞
#define MOD 1000000007 //10^9+7:合同式の法
#define MAXR 100000 //10^5:配列の最大のrange(素数列挙などで使用)
//略記
#define PB push_back //vectorヘの挿入
#define MP make_pair //pairのコンストラクタ
#define PF pop_front
#define F first //pairの一つ目の要素
#define S second //pairの二つ目の要素

ll h,w,k;
vector<vector<ll>> dp;
deque<pair<ll,ll>> now;



void bfs(ll d){
    ll l=SIZE(now);
    if(l==0){
        return;
    }
    deque<vector<ll>> dp_sub;
    set<pair<ll,ll>> cand;
    REP(i,l){
        ll x,y;x=now.front().F;y=now.front().S;now.PF();
        FOR(j,1,min(k,w-y-1)){
            if(dp[x][y+j]==INF){
                dp_sub.PB({x,y+j,d});
                //dp[x][y+j]=d;
                cand.insert(MP(x,y+j));
                //now.PB(MP(x,y+j));
            }else{
                break;
            }
            //if(dp[x][y+j]==-1)break;
        }
        FOR(j,1,min(k,y)){
            if(dp[x][y-j]==INF){
                dp_sub.PB({x,y-j,d});
                //dp[x][y-j]=d;
                cand.insert(MP(x,y-j));
                //now.PB(MP(x,y-j));
            }else{
                break;
            }
            //if(dp[x][y-j]==-1)break;
        }
        FOR(j,1,min(k,h-x-1)){
            if(dp[x+j][y]==INF){
                dp_sub.PB({x+j,y,d});
                //dp[x+j][y]=d;
                cand.insert(MP(x+j,y));
                //now.PB(MP(x+j,y));
            }else{
                break;
            }
            //if(dp[x+j][y]==-1)break;
        }
        FOR(j,1,min(k,x)){
            if(dp[x-j][y]==INF){
                dp_sub.PB({x-j,y,d});
                //dp[x-j][y]=d;
                cand.insert(MP(x-j,y));
                //now.PB(MP(x-j,y));
            }else{
                break;
            }
            //if(dp[x-j][y]==-1)break;
        }
    }
    while(!dp_sub.empty()){
        vector<ll> d=dp_sub.front();
        dp[d[0]][d[1]]=d[2];
        dp_sub.PF();
    }
    for(auto i=cand.begin();i!=cand.end();i++){
        now.PB(*i);
    }
    bfs(d+1);
}
signed main(){
    //入力の高速化用のコード
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cin >> h >> w >>k;
    ll x1,y1,x2,y2;cin >> x1 >> y1 >> x2 >> y2;
    vector<string> c(h);REP(i,h)cin >> c[i];
    dp.resize(h);
    REP(i,h){
        REP(j,w){
            if(c[i][j]=='.')dp[i].PB(INF);
            else dp[i].PB(-1); 
        }
    }
    now.PB(MP(x1-1,y1-1));
    dp[x1-1][y1-1]=0;
    bfs(1);
    if(dp[x2-1][y2-1]!=INF) cout << dp[x2-1][y2-1] << endl;
    else cout << -1 << endl;
}