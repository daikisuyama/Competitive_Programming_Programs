//デバッグ用オプション：-fsanitize=undefined,address

//コンパイラ最適化
#pragma GCC optimize("Ofast")

//インクルードなど
#include<bits/stdc++.h>
using namespace std;
typedef double ll;

//マクロ
//forループ
//引数は、(ループ内変数,動く範囲)か(ループ内変数,始めの数,終わりの数)、のどちらか
//Dがついてないものはループ変数は1ずつインクリメントされ、Dがついてるものはループ変数は1ずつデクリメントされる
//FORAは範囲for文(使いにくかったら消す)
#define REP(i,n) for(int i=0;i<int(n);i++)
#define FOR(i,a,b) for(int i=a;i<=int(b);i++)
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
#define EPS 0.000000000000001

vector<ll> dist;
vector<vector<pair<int,ll>>> edges;

void dijkstra(ll f){
    priority_queue<pair<ll,int>,vector<pair<ll,int>>,greater<pair<ll,int>>> q;
    q.push({0.0,f});
    while(!q.empty()){
        pair<ll,int> next=q.top();q.pop();
        //cout<<dist[next.S]<<next.F+EPS<<endl;
        //cout<<next.S<<endl;
        if(dist[next.S]<next.F+EPS) continue;
        dist[next.S]=next.F;
        for(const auto& edge:edges[next.S]){
            //cout<<dist[edge.F]<<" "<<next.F+edge.F+EPS<<endl;
            if(dist[edge.F]<next.F+edge.F+EPS) continue;
            q.push({next.F+edge.S,edge.F});
        }
    }
}

//負にならないように(途中で通る場合もあるのか)
ll distcalc(vector<long long>& f1,vector<long long>& f2){
    return max(ll(0),sqrt((f1[0]-f2[0])*(f1[0]-f2[0])+(f1[1]-f2[1])*(f1[1]-f2[1]))-f1[2]-f2[2]);
}


//llはdouble
signed main(){
    //入力の高速化用のコード
    //ios::sync_with_stdio(false);
    //cin.tie(nullptr);
    //小数点誤差
    //INF初期化
    //INFの大きさ
    //int足してlong long を超える
    cout<<fixed<<setprecision(10);
    long long xs,ys,xt,yt;cin>>xs>>ys>>xt>>yt;
    int n;cin>>n;
    vector<vector<long long>> points(n+2);
    points[0]={xs,ys,0};points[n+1]={xt,yt,0};
    FOR(i,1,n){
        int x,y,r;cin>>x>>y>>r;
        points[i]={x,y,r};
    }
    dist=vector<ll>(n+2,ll(INF));
    edges.resize(n+2);
    REP(i,n+2){
        REP(j,n+2){
            if(i!=j)edges[i].PB({j,distcalc(points[i],points[j])});
        }
    }
    dijkstra(0);
    cout<<dist[n+1]<<endl;
}