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

ll rec(vector<ll> vec,ll ind){
    ll ret=0;
    vector<ll> vec0,vec1;
    FORA(i,vec){
        if((i>>ind)&1){
            vec0.PB(i);
        }else{
            vec1.PB(i);
        }
    }
    if(SIZE(vec0)==0){
        if(ind==0)return 0;
        return rec(vec1,ind-1);
    }
    if(SIZE(vec1)==0){
        if(ind==0)return 0;
        return rec(vec0,ind-1);
    }
    //どちらも0でない(小さい方を返す)
    //+2^iか
    if(ind==0)return 1;
    return min(rec(vec0,ind-1),rec(vec1,ind-1))+(1<<ind);
}

signed main(){
    //入力の高速化用のコード
    //ios::sync_with_stdio(false);
    //cin.tie(nullptr);
    ll n;cin>>n;
    vector<ll> a(n);REP(i,n)cin>>a[i];
    cout<<rec(a,31)<<endl;
}