//コンパイラ最適化用
#pragma GCC optimize("Ofast")
//インクルード(アルファベット順)
#include<bits/stdc++.h>
using namespace std;
typedef int ll;

#define REP(i,n) for(ll i=0;i<n;i++)
//xにはvectorなどのコンテナ
#define SIZE(x) ll(x.size())
#define PB push_back //vectorヘの挿入
#define MP make_pair //pairのコンストラクタ
#define F first //pairの一つ目の要素
#define S second //pairの二つ目の要素
#define Umap unordered_map

signed main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    ll n;cin>>n;
    vector<vector<ll>> a(n,vector<ll>(n-1));
    REP(i,n){
        REP(j,n-1){
            ll c;cin>>c;
            if(c-1<i)a[i][j]=c-1+n*i;
            else a[i][j]=i+n*(c-1);
        }
    }
    Umap<ll,ll> d;
    REP(i,n)d[a[i][0]]++;
    vector<ll> b(n,0);
    ll ans=0;
    deque<ll> nextd;
    deque<ll> cleard;
    while(!d.empty()){
        ans++;
        bool g=true;
        for(const auto& i : d){
            if(i.S==2){
                g=false;
                ll e=(i.F)/n;ll f=(i.F)%n;
                cleard.insert(cleard.begin(),i.F);
                b[e]++;b[f]++;
                if(b[e]<n-1)nextd.insert(nextd.begin(),a[e][b[e]]);
                if(b[f]<n-1)nextd.insert(nextd.begin(),a[f][b[f]]);
            }
        }
        if(g){
            cout<<-1<<endl;
            return 0;
        }
        ll ln,lc;ln=SIZE(nextd);lc=SIZE(cleard);
        REP(i,ln){
            d[*--nextd.end()]++;
            nextd.pop_back();
        }
        REP(i,lc){
            d.erase(*--cleard.end());
            cleard.pop_back();
        }
    }
    cout<<ans<<endl;
    return 0;
}