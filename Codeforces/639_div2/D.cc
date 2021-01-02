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

deque<pair<ll,ll>> d;
vector<vector<bool>> bfs_chk;
ll n,m;

void bfs(){
    while(SIZE(d)){
        ll l=SIZE(d);
        REP(i,l){
            ll c0,c1;c0=d.front().F;c1=d.front().S;
            //cout<<c0<<" "<<c1<<endl;
            vector<pair<ll,ll>> nex={MP(c0-1,c1),MP(c0+1,c1),MP(c0,c1-1),MP(c0,c1+1)};
            FORA(j,nex){
                //cout<<1<<endl;
                if(0<=j.F and j.F<n and 0<=j.S and j.S<m){
                    //cout<<j.F<<" "<<j.S<<endl;
                    if(!bfs_chk[j.F][j.S]){
                        bfs_chk[j.F][j.S]=true;
                        d.PB(j);
                        //cout<<1<<endl;
                    }
                }
            }
            d.pop_front();
        }
    }
}

signed main(){
    //入力の高速化用のコード
    //ios::sync_with_stdio(false);
    //cin.tie(nullptr);
    cin>>n>>m;
    vector<string> s(n);REP(i,n)cin>>s[i];
    bfs_chk=vector<vector<bool>>(n,vector<bool>(m,true));
    REP(i,n)REP(j,m)bfs_chk[i][j]=(s[i][j]=='.');
    ll ans=0;
    //cout<<1<<endl;
    REP(i,n){
        REP(j,m){
            if(bfs_chk[i][j]==false){
                bfs_chk[i][j]=true;
                d.PB(MP(i,j));
                bfs();
                ans++;
            }
        }
    }
    //cout<<1<<endl;
    vector<bool> r(n,false);
    vector<bool> c(m,false);
    REP(i,n){
        REP(j,m){
            if(s[i][j]=='#'){
                FOR(k,j,m-1){
                    if(s[i][k]=='.'){
                        FOR(l,k,m-1){
                            if(s[i][l]=='#'){
                                //cout<<2<<endl;
                                cout<<-1<<endl;
                                return 0;
                            }
                        }
                        break;
                    }else{
                        c[j]=true;
                        r[i]=true;
                    }
                }
                break;
            }
        }
    }
    REP(i,m){
        REP(j,n){
            if(s[j][i]=='#'){
                FOR(k,j,n-1){
                    if(s[k][i]=='.'){
                        FOR(l,k,n-1){
                            if(s[l][i]=='#'){
                                //cout<<3<<endl;
                                cout<<-1<<endl;
                                return 0;
                            }
                        }
                        break;
                    }else{
                        r[j]=true;
                        c[i]=true;
                    }
                }
                break;
            }
        }
    }

    //追加できる場合
    pair<vector<ll>,vector<ll>> addition;
    REP(i,n){
        ll co=0;
        REP(j,m){
            co+=ll(s[i][j]=='#');
        }
        if(co==0)addition.F.PB(i);
    }
    REP(j,m){
        ll co=0;
        REP(i,n){
            co+=ll(s[i][j]=='#');
        }
        if(co==0)addition.S.PB(j);
    }
    FORA(i,addition.F){
        FORA(j,addition.S){
            r[i]=true;
            c[j]=true;
        }
    }

    //REP(i,n)cout<<r[i]<<endl;
    //REP(i,m)cout<<c[i]<<endl;
    if(all_of(ALL(r),[](bool x){return x;}) and all_of(ALL(c),[](bool x){return x;})){
        cout<<ans<<endl;
    }else if(all_of(ALL(r),[](bool x){return !x;}) and all_of(ALL(c),[](bool x){return !x;})){
        cout<<ans<<endl;
    }else{
        //cout<<4<<endl;
        cout<<-1<<endl;
    }
}