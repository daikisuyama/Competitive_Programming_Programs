#include<bits/stdc++.h>
using namespace std;
typedef long long ll;

#define REP(i,n) for(ll i=0;i<ll(n);i++)
#define INF64 9223372036854775807

signed main(){
    ll v,e;cin>>v>>e;
    //隣接行列
    //graph[i][j]:=i→jの辺の長さ,繋がってない場合はINF64で初期化
    vector<vector<ll>> graph(v,vector<ll>(v,INF64));
    REP(i,e){
        ll s,t,d;cin>>s>>t>>d;
        graph[s][t]=d;
    }
    //以降、"頂点の部分集合"を"部分集合"と簡略化して表記
    //dp[i][j]:=(部分集合iで最後に到達したのが頂点jでの最短距離)
    vector<vector<ll>> dp;
    //解として求める最小値
    ll ans=INF64;
    //始点をどの頂点にするか(v通り)
    REP(l,v){
        //それぞれの始点からのDP
        dp=vector<vector<ll>>(1LL<<v,vector<ll>(v,INF64));
        //始点→始点の最短距離は0で初期化
        dp[1LL<<l][l]=0;
        //任意の部分集合からの遷移を考える
        REP(i,(1LL<<v)){
            //最後に到達した頂点j
            REP(j,v){
                //その状態にならない場合は飛ばす
                if(dp[i][j]==INF64)continue;
                //次に到達する頂点k
                REP(k,v){
                    //j→kに辺が繋がっているか
                    if(graph[j][k]==INF64)continue;
                    //部分集合iにすでに含まれている場合は飛ばす(一回ずつという条件より)
                    //この処理ができない場合はbitDPでは解けない
                    if((i>>k)&1)continue;
                    //dpの更新
                    //chmin(dp[部分集合iに頂点kを追加した部分集合][最後に到達した頂点k],dp[部分集合i][最後に到達していた頂点j]+(j→kの頂点間の距離))
                    dp[i|(1LL<<k)][k]=min(dp[i|(1LL<<k)][k],dp[i][j]+graph[j][k]);
                }
            }
        }
        //dp[全頂点の集合]で最小値を考える
        //最後に到達した頂点がi
        REP(i,v){
            //その状態が存在しない場合,iから始点lに戻れない場合
            if(dp[(1LL<<v)-1][i]==INF64 or graph[i][l]==INF64)continue;
            //それ以外の場合はchminを考える
            ans=min(dp[(1LL<<v)-1][i]+graph[i][l],ans);
        }
    }
    //状態として存在しない場合は-1、それ以外はそのまま出力
    if(ans==INF64){
        cout<<-1<<endl;
    }else{
        cout<<ans<<endl;
    }
}