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
#define MOD 1000000 //10^9+7:合同式の法
#define MAXR 100000 //10^5:配列の最大のrange
//略記
#define PB push_back //挿入
#define MP make_pair //pairのコンストラクタ
#define F first //pairの一つ目の要素
#define S second //pairの二つ目の要素

signed main(){
    //入力の高速化用のコード
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    ll h,w;cin>>h>>w;
    //終点,始点を管理
    set<ll> tofrom;
    //最小を管理
    multiset<ll> cost;
    REP(i,w){
        tofrom.insert(i*MOD+i);
        cost.insert(0);
    }
    REP(i,h){
        ll a,b;cin>>a>>b;a--;b--;
        auto j=tofrom.lower_bound(a*MOD);
        if(j!=tofrom.end()){
            ll ne=-1;
            while(j!=tofrom.end() or *j<(b+2)*MOD){
                cost.erase(cost.lower_bound(ll(*j/MOD)-*j%MOD));
                ne=*j%MOD;
                j=tofrom.erase(j);
            }
            if(b==w-1){
                cost.insert(INF);
            }else{
                cost.insert(b+1-ne);
                tofrom.insert((b+1)*MOD+ne);
            }
        }
        if(*cost.begin()!=INF)cout<<*cost.begin()+i+1<<"\n";
        else cout<<-1<<"\n";
    }
}