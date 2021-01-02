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
    ll m;cin>>m;
    REP(_,m){
        ll n,t,a,b;cin>>n>>t>>a>>b;
        vector<ll> level(n);REP(i,n)cin>>level[i];
        vector<ll> tim(n);REP(i,n)cin>>tim[i];
        //追加で解いても良い問題(簡単なやつ,難しいやつ)
        ll easy=0;ll hard=0;
        //時刻に対してのlevel
        map<ll,vector<ll>> problem;
        REP(i,n){
            if(level[i]==0)easy++;
            else hard++;
            problem[tim[i]].PB(level[i]);
        }
        //最大のポイント
        ll ans=0;
        //今の合計のproblem数
        ll now=0;
        //ここまでの必要な時間
        ll s=0;
        FORA(i,problem){
            if(s<=i.F-1){
                if(s+easy*a>i.F-1){
                    ans=max(ans,ll(now+(i.F-1-s)/a));
                }else{
                    ans=max(ans,min(ll(now+easy+(i.F-1-s-easy*a)/b),now+easy+hard));
                }
            }
            FORA(j,i.S){
                if(j==0){
                    s+=a;
                    easy--;
                }else{
                    s+=b;
                    hard--;
                }
                now++;
            }
        }
        if(s<=t){
            ans=max(ans,now);
        }
        cout<<ans<<endl;
    }
}