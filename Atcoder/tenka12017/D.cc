//Codeforcesで128bit整数を使いたいとき
//→__int128_tを使う&GNU C++17 (64)で提出する
//デバッグ用オプション：-fsanitize=undefined,address

//コンパイラ最適化
#pragma GCC optimize("Ofast")

//インクルードなど
#include<bits/stdc++.h>
using namespace std;
typedef long long ll;

//マクロ
//forループ
//引数は、(ループ内変数,動く範囲)か(ループ内変数,始めの数,終わりの数)
//ループ内変数は1ずつインクリメント(orデクリメント(D)される)
//FORAは範囲for文
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

//aをbで割る時
//繰上げ,繰り下げ
ll myceil(ll a,ll b){return (a+(b-1))/b;}
ll myfloor(ll a,ll b){return a/b;}

ll msb(ll x){
    REPD(i,32){
        if((x>>i)&1){
            return i;
            break;
        }
    }
    return -1;
}

signed main(){
    //小数の桁数の出力指定
    //cout<<fixed<<setprecision(10);
    //入力の高速化用のコード
    //ios::sync_with_stdio(false);
    //cin.tie(nullptr);
    ll n,k;cin>>n>>k;
    ll m=msb(k);
    //同じ数はたしてしまえば(これで任意の数が異なる)
    map<ll,ll> nums_sub;
    REP(i,n){
        pair<ll,ll> x;cin>>x.F>>x.S;
        if(msb(x.F)<=m)nums_sub[x.F]+=x.S;
    }
    if(k==0){
        cout<<nums_sub[0]<<endl;
        return 0;
    }
    vector<pair<ll,ll>> nums;
    FORA(i,nums_sub)nums.PB(i);
    n=SIZE(nums);
    vector<ll> check(n,true);
    ll ans=0;
    FORD(i,m,0){
        if((k>>i)&1){
            ll ans_sub=0;
            REP(j,n){
                if((nums[j].F>>i)&1 or !check[j]){
                    if(i==0 and check[j])ans_sub+=nums[j].S;
                    continue;
                }else{
                    ans_sub+=nums[j].S;
                }
            }
            ans=max(ans,ans_sub);
        }else{
            REP(j,n){
                if((nums[j].F>>i)&1 and check[j]){
                    check[j]=false;
                }
            }
            if(i==0){
                ll ans_sub=0;
                REP(j,n){
                    if(check[j])ans_sub+=nums[j].S;
                }
                ans=max(ans,ans_sub);
            }
        }
    }
    cout<<ans<<endl;
}