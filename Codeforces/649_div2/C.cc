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
    vector<ll> a(n);
    set<ll> b;
    REP(i,n){
        cin>>a[i];
        b.insert(a[i]);
    }
    vector<ll> ans(n);
    set<ll> check;
    REP(i,a[n-1])check.insert(i);
    FORD(i,n-1,1){
        if(a[i]!=a[i-1]){
            ans[i]=a[i-1];
            check.erase(a[i-1]);
        }else{
            if(SIZE(check)==0){
                ans[i]=a[n-1]+1;
            }else{
                ll b=*--check.end();
                if(b<a[i]){
                    ans[i]=a[n-1]+1;
                }else{
                    ans[i]=b;
                    check.erase(b);
                }
            }
        }
    }
    //最後の処理だけ、カス
    if(SIZE(check)==0){
        ans[0]=a[n-1]+1;
    }else{
        ll b=*--check.end();
        ans[0]=b;
        check.erase(b);
    }
    if(SIZE(check)!=0){
        cout<<-1<<endl;
        return 0;
    }
    REP(i,n){
        if(i!=n-1)cout<<ans[i]<<" ";
        else cout<<ans[i]<<endl;
    }
}