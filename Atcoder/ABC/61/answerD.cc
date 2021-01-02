#include<iostream>
#include<algorithm>
#include<utility>
#include<vector>
using namespace std;
typedef long long ll;
//ここ十分にしないとだめ
#define INF 1000000000000

struct Node{
  //ノードの情報
  vector<pair<ll,ll>> edge;//各エッジの接続先のノード番号とコスト
  //ベルマンフォード法用のデータ
  ll mincost=INF;//そのノードへの最小コスト
};

//関係ないループを外す
bool bellmanford(vector<Node>& nodes,ll l1){
  //(l1-1)(普通のbellman)+1(検出)
  for(ll i=0;i<l1;i++){
    for(ll j=0;j<l1;j++){
      Node x=nodes[j];
      if(x.mincost!=INF){
        ll l2=x.edge.size();
        for(ll k=0;k<l2;k++){
          ll a=x.mincost+x.edge[k].second;
          if(nodes[x.edge[k].first].mincost>a){
            nodes[x.edge[k].first].mincost=a;
            if(i==l1-1 and x.edge[k].first==l1-1) return true;//負の閉路があればtrue
          }
        }
      }
    }
  }
  return false;//負の閉路がなければfalse
}

int main(){
  ll n,m;cin >> n >> m;
  vector<Node> Nodes(n);
  //mincost0の更新だけしっかりやる
  Nodes[0].mincost=0;

  for(ll i=0;i<m;i++){
    ll a,b,c;cin >> a >> b >> c;
    Nodes[a-1].edge.push_back(make_pair(b-1,-c));
  }
  //Nodesを更新
  if(bellmanford(Nodes,n)){
    cout << "inf" << endl;
  }else{
    cout << -Nodes[n-1].mincost << endl;
  }
}
