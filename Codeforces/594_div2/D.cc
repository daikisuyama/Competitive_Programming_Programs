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
    string s;cin>>s;
    ll ma=0;pair<ll,ll> now={1,1};
    if(n%2!=0 or ll(count(ALL(s),'('))!=ll(n/2)){
        cout<<0<<endl;
        cout<<"1 1"<<endl;
        return 0;
    }
    vector<ll> checks(n);
    REP(i,n){
        if(s[i]=='('){
            checks[i]=1;
        }else{
            checks[i]=-1;
        }
    }
    REP(i,n){
        REP(j,n){
            vector<ll> check=checks;
            swap(check[i],check[j]);
            //前から累積和をとる
            vector<ll> asum1(n);asum1[0]=check[0];
            REP(k,n-1)asum1[k+1]=asum1[k]+check[k+1];
            //後ろから累積和をとる
            vector<ll> asum2(n);asum2[n-1]=check[n-1];
            REPD(k,n-1)asum2[k]=asum2[k+1]+check[k];
            //前から累積最小をとる(累積和で)
            vector<ll> amin1(n);amin1[0]=asum1[0];
            REP(k,n-1)amin1[k+1]=min(amin1[k],asum1[k+1]);
            //後ろから累積最小をとる(累積和で)
            vector<ll> amin2(n);amin2[n-1]=asum1[n-1];
            REPD(k,n-1)amin2[k]=min(amin2[k+1],asum1[k]);

            ll ans=0;
            if(amin1[n-1]>=0)ans++;
            REP(k,n-1){
                if(amin2[k+1]-asum1[k]>=0 and amin1[k]+asum2[k+1]>=0){
                    ans++;
                }
            }
            if(ma<ans){
                ma=ans;
                now={i+1,j+1};
            }
        }
    }
    cout<<ma<<endl;
    cout<<now.F<<" "<<now.S<<endl;
}