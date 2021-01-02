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

//nは含まれない
set<ll> divisors;//約数を格納するset(削除したいので)

void make_divisors(ll n){
    FOR(i,2,sqrt(n)){
        if(n%i==0){
            divisors.insert(i);
            if(i!=n/i){
                divisors.insert(n/i);
            }
        }
    }
}

set<ll> prime;//素因数分解でそれぞれの素数がいくつ出てきたかを保存するmap

//O(√n)
//整列済み(mapはkeyで自動で整列される)
void prime_factorize(ll n){
    if(n<=1) return;
    ll l=sqrt(n);
    FOR(i,2,l){
        if(n%i==0){
        prime_factorize(i);prime_factorize(ll(n/i));return;
        }
    }
    //mapでは存在しないkeyの場合も自動で構築される
    prime.insert(n);return;
}

signed main(){
    //入力の高速化用のコード
    //ios::sync_with_stdio(false);
    //cin.tie(nullptr);
    ll t;cin>>t;
    REP(_,t){
        ll n;cin>>n;
        vector<ll> ans;
        divisors.clear();
        prime.clear();
        make_divisors(n);
        prime_factorize(n);
        if(SIZE(prime)==2 and (*prime.begin())*(*++prime.begin())==n){
            cout<<*prime.begin()<<" "<<*++prime.begin()<<" "<<n<<endl;
            cout<<1<<endl;
            continue;
        }
        for(auto i=prime.begin();i!=prime.end();i++){
            deque<ll> sub;
            ll l,r;l=*i;r=0;
            if(++i!=prime.end()){
                r=*i;
                sub.PB(l*r);
                divisors.erase(l*r);
            }
            --i;
            auto j=divisors.begin();
            while(j!=divisors.end()){
                if((*j)%(*i)==0){
                    sub.PB(*j);
                    j=divisors.erase(j);
                }else{
                    j++;
                }
            }
            while(SIZE(sub)){
                ll p=sub.back();
                sub.pop_back();
                ans.PB(p);
            }
        }
        ans.PB(n);
        if(SIZE(prime)==2 and (*prime.begin())*(*++prime.begin())==n){
            REP(i,SIZE(ans)){
                if(i!=SIZE(ans)-1)cout<<ans[i]<<" ";
                else cout<<ans[i]<<endl;
            }
            cout<<1<<endl;
        }else{
            REP(i,SIZE(ans)){
                if(i!=SIZE(ans)-1)cout<<ans[i]<<" ";
                else cout<<ans[i]<<endl;
            }
            cout<<0<<endl;
        }
    }
}