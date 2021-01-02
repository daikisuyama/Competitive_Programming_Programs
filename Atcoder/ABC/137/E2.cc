//コンパイラ最適化用
#pragma GCC optimize("O3")
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
#define REP(i,n) for(ll i=0;i<ll(n);i++)
#define REPD(i,n) for(ll i=n-1;i>=0;i--)
#define FOR(i,a,b) for(ll i=a;i<=ll(b);i++)
#define FORD(i,a,b) for(ll i=a;i>=ll(b);i--)
//xにはvectorなどのコンテナ
#define ALL(x) x.begin(),x.end() //sortなどの引数を省略したい
#define SIZE(x) ll(x.size()) //sizeをsize_tからllに直しておく
//定数
#define INF 1000000000000 //10^12:極めて大きい値,∞
#define MOD 1000000007 //10^9+7:合同式の法
#define MAXR 100000 //10^5:配列の最大のrange(素数列挙などで使用)
//略記
#define PB push_back //vectorヘの挿入
#define MP make_pair //pairのコンストラクタ
#define F first //pairの一つ目の要素
#define S second //pairの二つ目の要素
#define Umap unordered_map
#define Uset unordered_set

vector<ll> dist;
vector<vector<vector<ll>>> edges;
vector<bool> ncycle;
deque<ll> bfsrec;

//負閉路検出
void bfs(){
    ll s=SIZE(bfsrec);
    REP(i,s){
        ll now=bfsrec.front();
        for(const auto& edge:edges[now]){
            if(ncycle[edge[0]]==false){
                ncycle[edge[0]]=true;
                bfsrec.PB(edge[0]);
            }
        }
        bfsrec.pop_front();
    }
    if(s)bfs();
}

bool spfa(ll n,ll s){
    deque<ll> q;
    vector<bool> inq(n);
    vector<ll> co(n); 
    q.PB(s);
    inq[s]=0;
    ++co[s];
    while(!q.empty()){
        ll now=q.front();
        inq[now]=false;
        for(const auto& edge:edges[now]){
            ll new_dist=dist[now]+edge[1];
            if(dist[edge[0]]>new_dist){
                dist[edge[0]]=new_dist;
                if(!inq[edge[0]]){
                    if(co[edge[0]]!=n-1){
                        q.PB(edge[0]);
                        inq[edge[0]]=true;
                        ++co[edge[0]];
                    }else{
                        bfsrec.PB(edge[0]);
                    }
                }
            }
        }
        q.pop_front();
    }
    bfs();
    if(ncycle[n-1]==true)return true;
    return false;//Nを含む負の閉路がなければfalse
}


signed main(){
    //入力の高速化用のコード
    //ios::sync_with_stdio(false);
    //cin.tie(nullptr);
    ll n,m,p;cin>>n>>m>>p;
    dist.resize(n);dist[0]=0;
    FOR(i,1,n-1)dist[i]=INF;
    edges.resize(n);
    ncycle.resize(n);
    REP(i,n)ncycle[i]=false;
    //コストをpでマイナスしてそれを符号逆に
    REP(i,m){
        ll a,b,c;cin>>a>>b>>c;
        edges[a-1].PB({b-1,p-c});
    }
    //このもとでの最小を考える
    bool check=spfa(n,0);
    if(check or dist[n-1]==INF){
        cout<<-1<<endl;
    }else{
        cout<<max(-dist[n-1],ll(0))<<endl;
    }
}