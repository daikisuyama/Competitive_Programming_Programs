//Codeforcesで128bit整数を使いたいとき
//→__int128_tを使う&GNU C++17 (64)で提出する
//デバッグ用オプション：-fsanitize=undefined,address

//コンパイラ最適化
#pragma GCC optimize("Ofast")

//インクルードなど
#include<bits/stdc++.h>
using namespace std;
typedef long long ll;

//イテレーション
#define REP(i,n) for(ll i=0;i<ll(n);i++)
#define REPD(i,n) for(ll i=n-1;i>=0;i--)
#define FOR(i,a,b) for(ll i=a;i<=ll(b);i++)
#define FORD(i,a,b) for(ll i=a;i>=ll(b);i--)
#define FORA(i,I) for(const auto& i:I)
//x:コンテナ
#define ALL(x) x.begin(),x.end() 
#define SIZE(x) ll(x.size()) 
//定数
#define INF32 2147483647 //2.147483647×10^{9}:32bit整数のinf
#define INF64 9223372036854775807 //9.223372036854775807×10^{18}:64bit整数のinf
#define MOD 1000000007 //問題による
//略記
#define PB push_back 
#define MP make_pair
#define F first
#define S second
//出力(空白区切りで昇順に)
#define coutALL(x) for(auto i=x.begin();i!=--x.end();i++)cout<<*i<<" ";cout<<*--x.end()<<endl;

//aをbで割る時の繰上げ,繰り下げ
ll myceil(ll a,ll b){return (a+(b-1))/b;}
ll myfloor(ll a,ll b){return a/b;}


signed main(){
    //小数の桁数の出力指定
    //cout<<fixed<<setprecision(10);
    //入力の高速化用のコード
    //ios::sync_with_stdio(false);
    //cin.tie(nullptr);
    ll n;cin>>n;
    vector<ll> p(n);
    REP(i,n)cin>>p[i];
    deque<ll> ans;
    while(true){
        if(p[0]!=0){
            ll q=p[0];
            ans.PB(0);
            swap(p[0],p[q]);
        }else{
            REP(i,n){
                if(p[i]==1){
                    FOR(j,i,n-1){
                        swap(p[j],p[(j+1)%n]);
                        ans.PB(j);
                    }
                    break;
                }
            }
        }
        bool f=true;
        REP(i,n){
            if(p[i]!=i){
                f=false;
                break;
            }
        }
        if(f){
            cout<<SIZE(ans)<<endl;
            FORA(i,ans)cout<<i<<endl;
            return 0;
        }
    }
}