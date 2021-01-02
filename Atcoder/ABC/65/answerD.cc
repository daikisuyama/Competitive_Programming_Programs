//プリム法とかいうのを使うらしい
//結構当たり前だから諦めずに頑張れよ、こういうところだぞ

#include<iostream>
#include<queue>
#include<utility>
#include<algorithm>
#include<cmath>
#include<vector>
using namespace std;
typedef long long ll;

class Edge{
public:
  ll to_Node;
  ll cost;
  Edge(ll t,ll c){
    to_Node=t;cost=c;
  }
};

//pr_queueは優先順位高い(<で右に来るやつ)のが先に取り出される
bool operator< (const Edge& a,const Edge& b){
    return a.cost > b.cost;
};

ll distance(vector<ll>& a,vector<ll>& b){
  return min({abs(a[0]-b[0]),abs(a[1]-b[1])});
}

int main(){
  ll n;cin >> n;
  vector< vector<ll> > v1(n,vector<ll>(3,0));
  vector< vector<ll> > v2(n,vector<ll>(3,0));
  //自作クラスのpr_queueどうする
  for(ll i=0;i<n;i++){
    ll x,y;cin >> x >> y;
    v1[i][0]=x;v1[i][1]=y;v1[i][2]=i;
    v2[i][0]=x;v2[i][1]=y;v2[i][2]=i;
  }
  sort(v1.begin(),v1.end(),[](vector<ll>& a,vector<ll>& b){return a[0] < b[0];});
  sort(v2.begin(),v2.end(),[](vector<ll>& a,vector<ll>& b){return a[1] < b[1];});

  //ここでそれぞれのNodeから伸びる辺をqueueに入れておく
  vector< queue<Edge> > edges_before(n);
  for(ll i=0;i<n-1;i++){
    edges_before[v1[i][2]].push(Edge(v1[i+1][2],distance(v1[i],v1[i+1])));
    edges_before[v1[i+1][2]].push(Edge(v1[i][2],distance(v1[i],v1[i+1])));
    edges_before[v2[i][2]].push(Edge(v2[i+1][2],distance(v2[i],v2[i+1])));
    edges_before[v2[i+1][2]].push(Edge(v2[i][2],distance(v2[i],v2[i+1])));
  }

  //0から始まるので0で初期化
  vector<bool> check(n,false);check[0]=true;
  priority_queue<Edge> edges;
  ll l=edges_before[0].size();
  for(ll i=0;i<l;i++){
    edges.push(edges_before[0].front());
    edges_before[0].pop();
  }

  ll cost_sum=0;
  Edge now=edges.top();
  int i=0;
  while(edges.size()!=0){
    //nowが訪問済みなのは明らか
    if(!check[now.to_Node]){
      check[now.to_Node]=true;
      cost_sum+=now.cost;
      int k=now.to_Node;
      ll l=edges_before[k].size();
      edges.pop();//nowを除く(to_Nodeさえわかっていれば良いので)
      for(ll i=0;i<l;i++){
        Edge s=edges_before[k].front();
        if(!check[s.to_Node]) edges.push(s);
        edges_before[k].pop();
      }
      now=edges.top();
      //大して早くならなかった↓
      if(++i==n-1)break;
    }else{
      edges.pop();now=edges.top();
    }
  }
  cout << cost_sum << endl;
}
