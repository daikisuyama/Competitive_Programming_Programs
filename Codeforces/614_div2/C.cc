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
    ll n,q;cin>>n>>q;
    set<ll> ss2,s2,s1;
    REP(_,q){
        ll r,c;cin>>r>>c;r--;c--;
        if(r==0){
            if(s1.find(c)==s1.end()){
                s1.insert(c);
                if(s2.find(c-1)!=s2.end()){
                    ss2.insert(c-1);
                }
                if(s2.find(c)!=s2.end()){
                    ss2.insert(c);
                }
                if(s2.find(c+1)!=s2.end()){
                    ss2.insert(c+1);
                }
            }else{
                s1.erase(c);
                if(ss2.find(c-1)!=ss2.end() and s1.find(c-2)==s1.end() and s1.find(c-1)==s1.end()){
                    ss2.erase(c-1);
                }
                if(ss2.find(c)!=ss2.end() and s1.find(c+1)==s1.end() and s1.find(c-1)==s1.end()){
                    ss2.erase(c);
                }
                if(ss2.find(c+1)!=ss2.end() and s1.find(c+2)==s1.end() and s1.find(c+1)==s1.end()){
                    ss2.erase(c+1);
                }
            }
        }else{
            if(s2.find(c)==s2.end()){
                s2.insert(c);
                if(s1.find(c-1)!=s1.end() or s1.find(c)!=s1.end() or s1.find(c+1)!=s1.end()){
                    ss2.insert(c);
                }
            }else{
                s2.erase(c);
                if(ss2.find(c)!=ss2.end()){
                    ss2.erase(c);
                }
            }
        }
        if(SIZE(ss2)){
            cout<<"No"<<endl;
        }else{
            cout<<"Yes"<<endl;
        }
    }
}