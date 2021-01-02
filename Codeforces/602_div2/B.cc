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
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    ll t;cin>>t;
    REP(_,t){
        ll n;cin>>n;
        vector<ll> q(n);REP(i,n)cin>>q[i];
        vector<ll> p(n,-1);
        vector<bool> check(n,false);
        p[0]=q[0];
        check[q[0]-1]=true;
        ll now=ll(p[0]==1);
        bool f=true;
        FOR(i,1,n-1){
            if(q[i]!=q[i-1]){
                if(check[q[i]-1]){
                    cout<<-1<<endl;
                    f=false;
                    break;
                }else{
                    check[q[i]-1]=true;
                    p[i]=q[i];
                }
            }else{
                while(true){
                    if(!check[now]){
                        check[now]=true;
                        p[i]=now+1;
                        now++;
                        break;
                    }
                }
                if(q[i]<p[i]){
                    cout<<-1<<endl;
                    f=false;
                    break;
                }
            }
        }
        if(f){
            REP(i,n){
                if(i==n-1)cout<<p[i]<<endl;
                else cout<<p[i]<<" ";
            }
        }
    }
}