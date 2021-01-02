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
    
    //cout<<1<<endl;
    ll f=0;ll g=0;
    REP(i,n){
        ll li=-1;ll ri=-1;
        //左端
        REP(j,m){
            if(s[i][j]=='#'){
                li=j;
                break;
            }
        }
        //右端
        REPD(j,m){
            if(s[i][j]=='#'){
                ri=j;
                break;
            }
        }
        if(li==-1 and ri==-1){
            f++;
            continue;
        }
        FOR(j,li,ri){
            if(s[i][j]!='#'){
                cout<<-1<<endl;
                return 0;
            }
        }
    }
    REP(j,m){
        ll ui=-1;ll di=-1;
        //上端
        REP(i,n){
            if(s[i][j]=='#'){
                ui=i;
                break;
            }
        }
        //下端
        REPD(i,n){
            if(s[i][j]=='#'){
                di=i;
                break;
            }
        }
        if(ui==-1 and di==-1){
            g++;
            continue;
        }
        FOR(i,ui,di){
            if(s[i][j]!='#'){
                cout<<-1<<endl;
                return 0;
            }
        }
    }
    //いい感じにsouthをおけない時
    if((f==0 and g!=0)or(f!=0 and g==0)){
        cout<<-1<<endl;
        return 0;
    }
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
    cout<<ans<<endl;
}