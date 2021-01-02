//セグき整理
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
const double PI=M_PI;
//略記
#define PB push_back //挿入
#define MP make_pair //pairのコンストラクタ
#define F first //pairの一つ目の要素
#define S second //pairの二つ目の要素

//1-indexed
/* BIT: RAQ対応BIT
    初期値は a_1 = a_2 = ... = a_n = 0
    ・add(l,r,x): [l,r) に x を加算する
    ・sum(i): a_1 + a_2 + ... + a_i を計算する
    計算量は全て O(logn)
*/
template <typename T>
struct BIT {
    int n;             // 要素数
    vector<T> bit[2];  // データの格納先
    BIT(int n_) { init(n_); }
    void init(int n_) {
        n = n_ + 1;
        for (int p = 0; p < 2; p++) bit[p].assign(n, 0);
    }

    void add_sub(int p, int i, T x) {
        for (int idx = i; idx < n; idx += (idx & -idx)) {
            bit[p][idx] += x;
        }
    }
    void add(int l, int r, T x) {  // [l,r) に加算
        add_sub(0, l, -x * (l - 1));
        add_sub(0, r, x * (r - 1));
        add_sub(1, l, x);
        add_sub(1, r, -x);
    }

    T sum_sub(int p, int i) {
        T s(0);
        for (int idx = i; idx > 0; idx -= (idx & -idx)) {
            s += bit[p][idx];
        }
        return s;
    }
    T sum(int i) { return sum_sub(0, i) + sum_sub(1, i) * i; }
};


//split関数のせいしね

signed main(){
    //入力の高速化用のコード
    //ios::sync_with_stdio(false);
    //cin.tie(nullptr);
    ll n,q;cin>>n>>q;
    vector<ll> length(n);REP(i,n)length[i]=1;
    BIT<ll> angle(n);
    //1-indexedでちょうどいい
    BIT<double> ansx(n);ansx.add(1,n+1,1);
    //初めから0
    BIT<double> ansy(n);
    //cout<<0<<endl;
    REP(_,q){
        ll t;cin>>t;
        if(t==0){
            ll i,x;cin>>i>>x;
            ll a=angle.sum(i)-angle.sum(i-1);ll d=length[i-1];
            angle.add(i,n+1,x-a);
            //角度の足し算
            ansx.add(i,n+1,d*cos(PI*x/180)-d*cos(PI*a/180));
            ansy.add(i,n+1,d*sin(PI*x/180)-d*sin(PI*a/180));
        }else if(t==1){
            ll i,e;cin>>i>>e;
            ll d=length[i-1];ll x=angle.sum(i)-angle.sum(i-1);
            ansx.add(i,i+1,e*cos(PI*x/180)-d*cos(PI*x/180));
            ansy.add(i,i+1,e*sin(PI*x/180)-d*sin(PI*x/180));
            length[i-1]=e;
        }else{
            ll i;cin>>i;
            cout<<ansx.sum(i)<<" "<<ansy.sum(i)<<endl;
        }
    }
}