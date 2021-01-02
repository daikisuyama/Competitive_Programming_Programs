#include<iostream>
#include<algorithm>
#include<utility>
#include<vector>
//#include<queue>
using namespace std;

struct Node{
  //ノードの情報
  int num;//ノードの番号
  vector<pair<int,int>> edge;//各エッジの接続先のノード番号とコスト

  //ダイクストラ法用のデータ
  bool confirmed;//確定ノードかどうか
  int mincost;//そのノードへの最小コスト(確定かどうかはconfirmedで決まる)
};

bool operator<(const Node node1,const Node node2){
  return node1.mincost < node2.mincost;
}
/*
bool compare_pair(const pair<int,int> x,const pair<int,int> y){
  return x.second < y.second;
}
*/

pair<vector<pair<int,int>>::iterator,vector<pair<int,int>>::iterator> dijkstra1(vector<Node> Nodex){
  //優先度の低いものを取りだす(popで)
  //取り出したものが接続するノードのmincostを取り出す
  vector<pair<int,int>> c;
  while(Nodex.size()!=0){
    vector<Node>::iterator x=min_element(Nodex.begin(),Nodex.end());
    x->confirmed=true;//これいらない気もする
    c.push_back(make_pair(x->num,x->mincost));
    for(auto i=x->edge.begin();i<x->edge.end();i++){
      vector<Node>::iterator k=Nodex.end();
      for(vector<Node>::iterator j=Nodex.begin();j<Nodex.end();j++){
        if(j->num==i->first){
          k=j;
          break;
        }
      }
      //この下、ループの中でできる、kを定義する必要もない
      if(k!=Nodex.end()){
        if(k->mincost==1000000000){
          k->mincost=x->mincost+ i->second;
        }else{
          //1000000000は十分に大きいのでこの下のみを書けば十分
          k->mincost=min(k->mincost,x->mincost+ i->second);
        }
      }
    }
    Nodex.erase(x);
  }
  sort(c.begin(),c.end());
  return make_pair(c.begin(),c.end());
}

int main(){
  int n,m;cin >> n >> m;
  vector<Node> Nodes(n);
  for(int i=0;i<n;i++){
    Nodes[i].num=i;
    Nodes[i].confirmed=false;
    if(i==0){
      //始まりのノードを確定済みにする
      Nodes[i].mincost=0;
    }else{
      Nodes[i].mincost=1000000000;
    }//int型の最大値に近い
  }

  for(int i=0;i<m;i++){
    int l,r,c;
    cin >> l >> r >> c;
    for(int j=l-1;j<r;j++){
      for(int k=j+1;k<r;k++){
        Nodes[j].edge.push_back(make_pair(k,c));
      }
    }
  }


  pair<vector<pair<int,int>>::iterator,vector<pair<int,int>>::iterator> d=dijkstra1(Nodes);
  vector<pair<int,int>>::iterator i= --d.second;
  if((*i).second==1000000000){
    cout << -1 << endl;
  }else{
    cout << (*i).second << endl;
  }
  /*
  for(vector<pair<int,int>>::iterator i=d.first;i<d.second;i++){
    cout << (*i).first << " " << (*i).second << endl;
  }
  */
}
