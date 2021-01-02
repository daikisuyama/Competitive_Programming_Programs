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

ll k;
vector<ll> cards;

//i番目の数を返す
inline ll quadrant(ll x,ll i){
    return ((x>>(2*i))&1)+((x>>(2*i+1))&1)*2;
}

signed main(){
    //入力の高速化用のコード
    //ios::sync_with_stdio(false);
    //cin.tie(nullptr);
    ll n;cin>>n>>k;
    //vectorを4進数に！(実質二進数)
    cards=vector<ll>(n);
    map<ll,ll> ma;
    vector<ll> po(k);
    REP(i,k)po[i]=1LL<<(2*i);
    REP(j,n){
        string s;cin>>s;
        ll calc=0;
        REP(i,k){
            if(s[i]=='S'){
                calc+=1*po[i];
            }else if(s[i]=='T'){
                calc+=2*po[i];
            }else{
                calc+=3*po[i];
            }
        }
        cards[j]=calc;
        ma[cards[j]]=j;
    }
    //candで候補管理するのを止める(3で割るだけ)
    //枝刈り？
    ll ans=0;
    REP(i,n){
        FOR(j,i+1,n-1){
            ll ne=0;
            REP(l,k){
                ll temp=quadrant(cards[i],l)*quadrant(cards[j],l);
                if(temp==1 or temp==6){
                    ne+=po[l];
                }else if(temp==3 or temp==4){
                    ne+=2*po[l];
                }else{
                    ne+=3*po[l];
                }
            }
            if(ma.find(ne)!=ma.end()){
                ans++;
            }
        }
    }
    cout<<ll(ans/3)<<endl;
}