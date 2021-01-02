#include<iostream>
#include<algorithm>
#include<utility>
#include<vector>
using namespace std;
typedef long long ll;
//ここ十分にしないとだめ
#define INF 1000000000000

struct Edge{
  ll to_Node;
  ll cost;
  Edge(ll t,ll c){to_Node=t;cost=c;}
};

//関係ないループを外す
bool bellmanford(vector< vector<Edge> >& Edges,vector<ll>& mincost,ll n){
  //(l1-1)(普通のbellman)+1(検出)
  for(ll i=0;i<n;i++){
    for(ll j=0;j<n;j++){
      if(mincost[j]!=INF){
        ll e=Edges[j].size();
        for(ll k=0;k<e;k++){
          ll new_mincost=mincost[j]+Edges[j][k].cost;
          if(mincost[Edges[j][k].to_Node]>new_mincost){
            mincost[Edges[j][k].to_Node]=new_mincost;
            if(i==n-1 and Edges[j][k].to_Node==n-1)return true;//負の閉路があればtrue
          }
        }
      }
    }
  }
  return false;//負の閉路がなければfalse
}

int main(){
  ll n,m;cin >> n >> m;
  vector<ll> mincost(n,INF);
  vector< vector<Edge> > Edges(n);
  //mincost0の更新だけしっかりやる
  mincost[0]=0;

  for(ll i=0;i<m;i++){
    ll a,b,c;cin >> a >> b >> c;
    Edges[a-1].push_back(Edge(b-1,-c));
  }
  //Nodesを更新
  if(bellmanford(Edges,mincost,n)){
    cout << "inf" << endl;
  }else{
    cout << -mincost[n-1] << endl;
  }
}
