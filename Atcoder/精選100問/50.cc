#include<bits/stdc++.h>
using namespace std;
typedef long long ll;

#define REP(i,n) for(ll i=0;i<ll(n);i++)
#define FORA(i,I) for(const auto& i:I)
#define INF64 9223372036854775807 //9.223372036854775807×10^{18}:64bit整数のinf
#define F first
#define S second

//変数が多いので構造体で管理
struct building{
    ll s,t,d,time;
};

signed main(){
    ll n,m;cin>>n>>m;
    //隣接行列にすべきだが、実装のしやすさでただのvectorにした
    //buildings[i]:=(頂点s→頂点tを結ぶ,距離はdでtimeまでに通り終わらなければならない)
    //s,tは0-indexed
    vector<building> buildings(2*m);
    REP(i,m){
        ll s,t,d,time;cin>>s>>t>>d>>time;
        buildings[2*i]={s-1,t-1,d,time};
        buildings[2*i+1]={t-1,s-1,d,time};
    }
    //以降、"頂点の部分集合"を"部分集合"と簡略化して表記
    //dp[i][j]:=(部分集合i,最後に到達した建物jでの(最短の時間,方法の総数))
    //{INF64,0}で初期化
    vector<vector<pair<ll,ll>>> dp(1LL<<n,vector<pair<ll,ll>>(n,{INF64,0}));
    //始点は0なのでdp[1<<0][0]={0,1}
    dp[1][0]={0,1};
    //任意の部分集合i
    REP(i,1LL<<n){
        //最後に到達した頂点j
        REP(j,n){
            //その状態にならない場合は飛ばす
            if(dp[i][j].F==INF64)continue;
            //頂点jからの移動先の候補を全て見る
            FORA(bu,buildings){
                //始点がjでない時は飛ばす
                if(bu.s!=j)continue;
                //部分集合iにすでに終点含まれている場合は飛ばす(一回ずつという条件より)
                //この処理ができない場合はbitDPでは解けない
                if((i>>bu.t)&1)continue;
                //t:その道を通り過ぎるまでにかかる時間
                ll t=dp[i][j].F+bu.d;
                //制限時間を満たすか？
                if(t<=bu.time){
                    //更新する場合
                    if(t<dp[i|(1LL<<bu.t)][bu.t].F){
                        dp[i|(1LL<<bu.t)][bu.t]={t,dp[i][j].S};
                    //すでに同じ時間で到達する場合は"方法の総数"を書き換えるだけ
                    }else if(t==dp[i|(1LL<<bu.t)][bu.t].F){
                        dp[i|(1LL<<bu.t)][bu.t].S+=dp[i][j].S;
                    }
                }
            }
        }
    }
    //dp[全頂点の集合]で最小値を考える
    //"方法の総数"も求めたいことに注意
    pair<ll,ll> ans={INF64,-1};
    //最後に到達した頂点がi
    REP(i,n){
        //その状態が存在しない場合
        if(dp[(1LL<<n)-1][i].F==INF64)continue;
        //以降、dpの更新処理と同じなので飛ばす
        FORA(bu,buildings){
            if(bu.s==i and bu.t==0){
                if(dp[(1LL<<n)-1][i].F+bu.d>bu.time)continue;
                if(dp[(1LL<<n)-1][i].F+bu.d<ans.F){
                    ans={dp[(1LL<<n)-1][i].F+bu.d,dp[(1LL<<n)-1][i].S};
                }else if(dp[(1LL<<n)-1][i].F+bu.d==ans.F){
                    ans.S+=dp[(1LL<<n)-1][i].S;
                }
            }
        }
    }
    //その状態が存在しない場合はIMPOSSIBLE
    if(ans.F==INF64){
        cout<<"IMPOSSIBLE"<<endl;
    }else{
        cout<<ans.F<<" "<<ans.S<<endl;
    }
}