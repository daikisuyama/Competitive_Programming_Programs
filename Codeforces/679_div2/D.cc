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
    //小数の桁数の出力指定
    //cout<<fixed<<setprecision(10);
    //入力の高速化用のコード
    //ios::sync_with_stdio(false);
    //cin.tie(nullptr);
    ll n;cin>>n;
    vector<ll> que(2*n,0);
    REP(i,2*n){
        string s;cin>>s;
        if(s=="-"){
            ll x;cin>>x;
            que[i]=x;
        }
    }
    set<ll> cand;
    vector<ll> ans(n);
    ll ind=n-1;
    REPD(i,2*n){
        if(que[i]!=0){
            cand.insert(que[i]);
        }else{
            if(SIZE(cand)==0){
                cout<<"NO"<<endl;
                return 0;
            }else{
                ll y=*cand.begin();
                ans[ind]=y;
                ind--;
                cand.erase(cand.begin());
            }
        }
    }
    ind++;
    REP(i,2*n){
        if(que[i]==0){
            cand.insert(ans[ind]);
            ind++;
        }else{
            ll y=*cand.begin();
            if(que[i]!=y){
                cout<<"NO"<<endl;
                return 0;
            }
            cand.erase(cand.begin());
        }
    }
    cout<<"YES"<<endl;
    REP(i,n){
        if(i==n-1)cout<<ans[i]<<endl;
        else cout<<ans[i]<<" ";
    }
}