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
    ll n;cin>>n;
    //今残っている数の保存(pairで)
    set<pair<ll,ll>> le;
    //値とインデックスの対応関係
    vector<ll> A(n);
    REP(i,n){
        ll x;cin>>x;
        le.insert(MP(x,i));
        A[i]=x;
    }
    //今残っているインデックスの保存
    set<ll> indices;
    REP(i,n)indices.insert(i);

    REP(i,ll(n/2)){
        pair<ll,ll> now=*le.begin();
        le.erase(le.begin());
        ll x=now.S;
        //cout<<x<<endl;
        indices.erase(x);
        ll a;
        if(indices.lower_bound(x)==indices.end()){
            a=*indices.begin();
        }else{
            a=*indices.lower_bound(x);
        }
        ll b;
        if(indices.upper_bound(x)==indices.begin()){
            b=*(--indices.end());
        }else{
            b=*(--indices.upper_bound(x));
        }
        indices.erase(a);indices.erase(b);
        A[x]=A[a]+A[b];
        indices.insert(x);
        le.insert(MP(A[x],x));
        le.erase(MP(A[a],a));le.erase(MP(A[b],b));
    }
    cout<<(*le.begin()).F<<endl;
}