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
#define MAXR 100000 //10^5:配列の最大のrange
//略記
#define PB push_back //挿入
#define MP make_pair //pairのコンストラクタ
#define F first //pairの一つ目の要素
#define S second //pairの二つ目の要素

ll n,a,b,da,db;
vector<vector<ll>> tree;
vector<ll> check;
vector<ll> check2;

signed main(){
    //入力の高速化用のコード
    //ios::sync_with_stdio(false);
    //cin.tie(nullptr);
    ll t;cin>>t;
    REP(_,t){
        cin>>n>>a>>b>>da>>db;
        tree=vector<vector<ll>>(n);
        REP(i,n-1){
            ll u,v;cin>>u>>v;
            tree[u-1].PB(v-1);
            tree[v-1].PB(u-1);
        }
        check=vector<ll>(n,INF);
        deque<ll> d={a-1};
        ll dep=0;
        while(SIZE(d)){
            ll l=SIZE(d);
            REP(i,l){
                ll now=d.front();
                check[now]=dep;
                FORA(j,tree[now]){
                    if(check[j]==INF)d.PB(j);
                }
                d.pop_front();
            }
            dep++;
        }
        check2=vector<ll>(n,INF);
        d={ll(distance(check.begin(),max_element(ALL(check))))};
        dep=0;
        while(SIZE(d)){
            ll l=SIZE(d);
            REP(i,l){
                ll now=d.front();
                check2[now]=dep;
                FORA(j,tree[now]){
                    if(check2[j]==INF)d.PB(j);
                }
                d.pop_front();
            }
            dep++;
        }
        //cout<<check[b-1]<<" "<<da<<endl;
        if(check[b-1]<=da){
            cout<<"Alice"<<endl;
            //cout<<1<<endl;
            continue;
        }
        
        if(min(db,*max_element(ALL(check2)))<=2*da){
            cout<<"Alice"<<endl;
        }else{
            cout<<"Bob"<<endl;
        }
    }
}