//深さ優先で、距離を+していけば良い
//xとyそれぞれについて

#include<iostream>
#include<vector>
#include<utility>
using namespace std;
typedef long long ll;
typedef vector< vector< pair<long long,long long> > > vvp;

//Nodeクラス作らない方がスマート、これ早く書けるように
void dfs(vvp& tree,vector<ll>& tree_len,vector<bool>& check,ll dep,ll now){
  tree_len[now]=dep;
  check[now]=true;
  ll l=tree[now].size();
  for(int i=0;i<l;i++){
    if(check[tree[now][i].first]==false) dfs(tree,tree_len,check,dep+tree[now][i].second,tree[now][i].first);
  }
}

int main(){
  ll n;cin >> n;
  vvp tree(n);//Nodeから伸びる辺の情報
  vector<ll> tree_len(n,0);//最短経路保持
  vector<bool> check(n,false);//辿ったかどうか(いらない説も)
  //nにして入力終わらねえってなった
  for(int i=0;i<n-1;i++){
    ll a,b,c;cin >> a >> b >> c;
    tree[a-1].push_back(make_pair(b-1,c));
    tree[b-1].push_back(make_pair(a-1,c));
  }
  ll q,k;cin >> q >> k;
  dfs(tree,tree_len,check,0,k-1);
  for(int i=0;i<q;i++){
    ll x,y;cin >> x >> y;
    cout << tree_len[x-1]+tree_len[y-1] << endl;
  }
}
//わけわからん数字出たらlong longにする
