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
    ll t;cin>>t;
    REP(i,t){
        ll n,p,k;cin>>n>>p>>k;
        vector<ll> a(n);REP(i,n)cin>>a[i];
        sort(ALL(a));
        vector<ll> cand(k,0);
        vector<ll> acc(n,0);
        acc[0]=a[0];
        REP(i,n-1){
            acc[i+1]=a[i+1]+acc[i];
        }
        REP(i,k){
            ll q=p;
            if(i!=0){
                q-=acc[i-1];
            }
            ll ret=0;
            if(q<0)continue;
            ret+=i;
            REP(j,(n-i)/k){
                if(a[i-1+(j+1)*k]<=q){
                    ret+=k;
                    q-=a[i-1+(j+1)*k];
                }else{
                    break;
                }
            }
            cand[i]=ret;
        }
        cout<<*max_element(ALL(cand))<<endl;
    }
}