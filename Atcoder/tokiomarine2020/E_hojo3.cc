//bit演算の右側はllでないと型変換されない
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

//マクロ
//forループ関係
//引数は、(ループ内変数,動く範囲)か(ループ内変数,始めの数,終わりの数)、のどちらか
#define REP(i,n) for(ll i=0;i<(ll)(n);i++)
#define FOR(i,a,b) for(ll i=a;i<=(ll)(b);i++)
//xにはvectorなどのコンテナ
#define ALL(x) (x).begin(),(x).end() //sortなどの引数を省略したい
#define SIZE(x) ((ll)(x).size()) //sizeをsize_tからllに直しておく
//定数
#define INF 1000000000000 //10^12:極めて大きい値,∞
#define MOD 1000000007 //10^9+7:合同式の法
#define MAXR 100 //10^5:配列の最大のrange(素数列挙などで使用)
//略記
#define PB push_back //vectorヘの挿入
#define MP make_pair //pairのコンストラクタ
#define F first //pairの一つ目の要素
#define S second //pairの二つ目の要素


signed main(){
    //入力の高速化用のコード
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    ll n,k,s,t;cin >> n >> k >> s >> t;
    vector<ll> b(n);REP(i,n)cin >> b[i];
    vector<ll> a;

    //(1)
    REP(i,n){
        bool f=true;
        REP(j,18){
            bool s_,t_,b_;s_=(s>>j)&1;t_=(t>>j)&1;b_=(b[i]>>j)&1;
            if(s_ and t_){
                if(!(b_)){
                    f=false;break;
                }
            }else if(!(s_) and !(t_)){
                if(b_){
                    f=false;break;
                }
            }else if(s_ and !(t_)){
                cout<<0<<endl;return 0;
            }
        }
        if(f)a.PB(b[i]);
    }
    n=SIZE(a);
    k=min(n,k);
    
    //(2)
    vector<pair<ll,ll>> bits;
    REP(i,18){
        ll f1=0;ll f2=0;
        REP(j,n){
            if((a[j]>>i)&1){
                f1+=(1LL<<j);
            }else{
                f2+=(1LL<<j);
            }
        }
        if(f1 and f2){
            bits.PB(MP(f1,f2));
        }else if(!((s>>i)&1) and (t>>i)&1){
            cout<<0<<endl;return 0;
        }
    }
    ll bits_len=SIZE(bits);

    //(3)
    vector<vector<ll>> pcalc(n+1,vector<ll>(k+1,0));
    pcalc[0][0]=1;
    FOR(i,1,n){
        pcalc[i][0]=1;
        FOR(j,1,k){
            pcalc[i][j]=pcalc[i-1][j-1]+pcalc[i-1][j];
        }
    }
    REP(i,n+1){
        pcalc[i][0]=0;
        REP(j,k){
            pcalc[i][j+1]+=pcalc[i][j];
        }
    }

    //(4)
    ll ans_sub=0;
    deque<ll> all_sets;
    FOR(i,1,(1LL<<bits_len)-1){
        //(5)
        all_sets.PB((1LL<<n)-1);
        ll odd_even=0;
        REP(j,bits_len){
            if((i>>j)&1){
                odd_even+=1;
                ll s=SIZE(all_sets);
                REP(_,s){
                    ll ins=*(all_sets.begin());
                    all_sets.pop_front();
                    ll f1=ins&(bits[j].F);ll f2=ins&(bits[j].S);
                    if(f1){all_sets.PB(f1);}
                    if(f2){all_sets.PB(f2);}
                }
            }
        }
        
        //(6)
        ll s=SIZE(all_sets);
        REP(_,s){
            ll now=*(all_sets.begin());
            all_sets.pop_front();
            ll s_sub=__builtin_popcountll(now);
            if(odd_even%2){
                ans_sub+=pcalc[s_sub][min(k,s_sub)];
            }else{
                ans_sub-=pcalc[s_sub][min(k,s_sub)];
            }
        }
    }
    //(7)
    cout<< pcalc[n][k]-ans_sub <<endl;
}
