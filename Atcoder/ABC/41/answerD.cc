//以下bitDP
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
#define REP(i,n) for(int i=0;i<(int)(n);i++)
#define REPD(i,n) for(int i=(int)(n)-1;i>=0;i--)
#define FOR(i,a,b) for(int i=(a);i<=(b);i++)
#define FORD(i,a,b) for(int i=(a);i>=(b);i--)
#define ALL(x) (x).begin(),(x).end() //sortなどの引数を省略したい
#define SIZE(x) ((int)(x).size()) //sizeをsize_tからintに直しておく
#define INF 1000000000000
#define MOD 10000007
#define PB push_back
#define MP make_pair
#define F first
#define S second

signed main(){
    int n,m;cin >> n >> m;const int k=pow(2,n)-1;
    vector< vector<int> > p(n,vector<int>(n,0));
    //まずは集合間の遷移を制限するように配列pを用意する。
    REP(i,m){
        int x,y;cin >> x >> y;
        p[y-1][x-1]=1;
    }
    //1~nのウサギをn回加えてく(すでにある場合は加えない)
    vector<ll> dp(k+1,0);dp[0]=1;
    REP(i,n){
        //同じウサギはいないので、dp_subとして一旦保存する。
        vector<ll> dp_sub(k+1,0);
        REP(j,k+1){
            //それぞれの集合をみていく
            if(dp[j]!=0){//その集合がその時点では実現していない場合
                REP(l,n){//集合内にn匹のどのウサギが含まれるかウサギを一匹ずつ見ていく
                    if(!((1<<l) & j)){//その集合に含まれない場合
                        //その集合に含まれないウサギを追加できるか計算する。
                        bool f=true;//追加できるならtrue、追加できないならfalse 
                        vector<int> now=p[l];//ウサギlより前にどのウサギが来るべきかを保持してある。
                        REP(r,n){//nowに順にアクセスする
                            //ウサギrがウサギlより前にいるべきか、ウサギrは集合に含まれるのかをチェックする。
                            if(now[r]==1 and (!((1<<r) & j))){
                                f=false;break;
                            }
                        }
                        //追加できるなら追加する。lが追加されると+2^l番目が増える。
                        if(f) dp_sub[j+int(pow(2,l))]+=dp[j];
                    }
                }
            }
        }
        //dp_subをdpに写す
        REP(j,k+1){
            dp[j]=dp_sub[j];
        }
    }
    cout << dp[k] << endl;
}