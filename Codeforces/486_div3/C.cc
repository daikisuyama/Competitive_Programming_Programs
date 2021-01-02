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

signed main(){
    //入力の高速化用のコード
    //ios::sync_with_stdio(false);
    //cin.tie(nullptr);
    ll k;cin>>k;
    map<ll,vector<pair<ll,ll>>> m;
    REP(i,k){
        ll ni;cin>>ni;
        vector<ll> a(ni);REP(j,ni)cin>>a[j];
        ll s=0;REP(j,ni)s+=a[j];
        REP(j,ni){
            m[s-a[j]].PB(MP(i+1,j+1));
        }
    }
    FORA(i,m){
        if(SIZE(i.S)>1){
            map<ll,ll> x;
            //同じ数列被り排除
            FORA(j,i.S){
                x[j.F]=j.S;
            }
            if(SIZE(x)>1){
                auto y=x.begin();
                cout<<"YES"<<endl;
                cout<<y->F<<" "<<y->S<<endl;
                y++;
                cout<<y->F<<" "<<y->S<<endl;
                return 0;
            }
        }
    }
    cout<<"NO"<<endl;
}