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

//1-indexed
class BIT {
public:
    ll n; //データの長さ
    vector<ll> bit; //データの格納先
    BIT(ll n):n(n),bit(n+1,0){} //コンストラクタ

    //k & -kはLSB

    //bit_iにxをO(log(n))で加算する
    void add(ll i,ll x){
        if(i==0) return;
        for(ll k=i;k<=n;k+=(k & -k)){
            bit[k]+=x;
        }
    }

    //bit_1 + bit_2 + …  + bit_n をO(log(n))で求める
    ll sum(ll i){
        ll s=0;
        if(i==0) return s;
        for(ll k=i;k>0;k-=(k & -k)){
            s+=bit[k];
        }
        return s;
    }

    //a_1 + a_2 + … + a_i >= x となるような最小のiを求める(a_k >= 0)
    //xが0以下の場合は該当するものなし→0を返す
    ll lower_bound(ll x){
        if(x<=0){
            return 0;
        }else{
            ll i=0;ll r=1;
            //最大としてありうる区間の長さを取得する
            //n以下の最小の二乗のべき(BITで管理する数列の区間で最大のもの)を求める
            while(r<n) r=r<<1;
            //区間の長さは調べるごとに半分になる
            for(int len=r;len>0;len=len>>1) {
                //その区間を採用する場合
                if(i+len<n && bit[i+len]<x){
                    x-=bit[i+len];
                    i+=len;
                }
            }
            return i+1;
        }
    }
};

signed main(){
    //入力の高速化用のコード
    //ios::sync_with_stdio(false);
    //cin.tie(nullptr);
    ll n,k;cin>>n>>k;
    vector<ll> a(n+1,-k);REP(i,n){cin>>a[i+1];a[i+1]-=k;}
    REP(i,n)a[i+1]+=a[i];
    set<ll> coco;REP(i,n+1)coco.insert(a[i]);
    //ind:1~
    map<ll,ll> check;
    ll j=0;
    FORA(i,coco){
        j++;
        check[i]=j;
    }
    BIT x(n+3);
    ll ans=0;
    REPD(i,n+1){
        ans+=(x.sum(n+3)-x.sum(check[a[i]]-1));
        x.add(check[a[i]],1);
    }
    cout<<ans<<endl;
}