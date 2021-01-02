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

vector<bool> check;
vector<vector<ll>> tree;


//実装を整理してイメージしような…
ll bfs(ll i){
    ll ret=1;
    deque<ll> d;
    deque<ll> e;
    check[i]=true;
    if(SIZE(tree[i])==0)return 0;
    e.PB(i);
    d.PB(tree[i][0]);
    e.PB(tree[i][0]);
    check[tree[i][0]]=true;
    //成り立つと仮定する
    while(SIZE(d)){
        ll l=SIZE(d);
        REP(_,l){
            ll p=d.front();
            d.pop_front();
            FORA(j,tree[p]){
                if(check[j]==false){
                    check[j]=true;
                    d.PB(j);
                    e.PB(j);
                }
            }
        }
    }
    //FORA(i,e)cout<<i<<" ";
    //cout<<endl;
    for(auto j=e.begin();j!=e.end();j++){
        ll x,y;x=*j;
        if(j==--e.end()){
            y=*e.begin();
        }else{
            //y=*jにしてた
            auto k=j;k++;y=*k;
        }
        if(SIZE(tree[x])!=2){
            ret=0;
            break;
        }else{
            if(tree[x][0]==y or tree[x][1]==y){
                continue;
            }else{
                ret=0;
                break;
            }
        }
    }
    d.PB(i);
    while(SIZE(d)){
        ll l=SIZE(d);
        REP(_,l){
            ll p=d.front();
            d.pop_front();
            FORA(j,tree[p]){
                if(check[j]==false){
                    check[j]=true;
                    d.PB(j);
                    e.PB(j);
                }
            }
        }
    }
    return ret;
}

signed main(){
    //入力の高速化用のコード
    //ios::sync_with_stdio(false);
    //cin.tie(nullptr);
    ll n,m;cin>>n>>m;
    tree=vector<vector<ll>>(n);
    check=vector<bool>(n,false);
    REP(i,m){
        ll u,v;cin>>u>>v;
        tree[u-1].PB(v-1);
        tree[v-1].PB(u-1);
    }
    ll ans=0;
    REP(i,n){
        if(check[i]==false){
            ans+=bfs(i);
        }
    }
    cout<<ans<<endl;
}