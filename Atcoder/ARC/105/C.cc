//貪欲法なのでWA


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
    ll n,m;cin>>n>>m;
    vector<ll> w(n);REP(i,n)cin>>w[i];
    sort(ALL(w));
    vector<pair<ll,ll>> partsx(m);
    //長さ,重さ
    REP(i,m)cin>>partsx[i].F>>partsx[i].S;
    sort(ALL(partsx));
    ll ma=INF;
    REP(i,m)ma=min(ma,partsx[i].S);
    //cout<<1<<endl;
    if(ma<w[n-1]){
        cout<<-1<<endl;
        return 0;
    }
    //cout<<1<<endl;
    //まず情報として意味あるパーツなのかを考える
    //(長さ,重さ)が(a,b),(c,d)でa>=cでb<=dのとき前者を満たしていれば良い
    //長さの上から下を見て残すかどうかをチェックする
    vector<bool> info(m,true);
    REPD(i,m){
        if(!info[i])continue;
        REP(j,i){
            if(partsx[i].S<=partsx[j].S){
                info[j]=false;
            }
        }
    }
    vector<pair<ll,ll>> parts;
    REP(i,m)if(info[i])parts.PB(partsx[i]);
    m=SIZE(parts);
    FORA(i,parts){
        cout<<i.F<<" "<<i.S<<endl;
    }
    ll ans=INF;
    do{
        //間の距離
        vector<ll> dist(n-1,0);
        REP(i,m){
            //j始まり(どこまで一緒のところ？)
            REP(j,n-1){
                //k:今の終わりのところ
                //check:そこまでの重さ
                //d:そこまでの距離
                ll k=j;ll check=w[j];ll d=0;
                while(true){
                    k++;
                    //ここの更新
                    if(k==n)break;
                    check+=w[k];
                    d+=dist[k-1];
                    if(parts[i].S<check){
                        if(parts[i].F>d){
                            dist[k-1]+=(parts[i].F-d);
                        }
                        break;
                    }else{
                        if(d>=parts[i].F){
                            break;
                        }
                    }
                }
            }
        }
        ans=min(ans,accumulate(ALL(dist),0LL));
    }while(next_permutation(w.begin(),w.end()));
    cout<<ans<<endl;
}