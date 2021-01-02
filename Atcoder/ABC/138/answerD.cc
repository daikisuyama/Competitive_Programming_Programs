#include<iostream>
#include<vector>
#include<string>
#include<queue>
#include<utility>

using namespace std;

int main(){
  int n,q;cin >> n >> q;
  vector< vector<int> > u(n);
  for(int i=0;i<n-1;i++){
    int a,b;cin >> a >> b;
    u[a-1].push_back(b-1);
    u[b-1].push_back(a-1);
  }

  vector<int> c(n,0);
  for(int i=0;i<q;i++){
    int p,x;cin >> p >> x;c[p-1]+=x;
  }
  //直前のも保持しておく
  queue< pair<int,int> > k;k.push(make_pair(-1,0));

  //幅優先探索
  while(k.size()!=0){
    int l1=k.size();
    for(int i=0;i<l1;i++){
      pair<int,int> a=k.front();
      int l2=u[a.second].size();
      for(int j=0;j<l2;j++){
        if(u[a.second][j]!=a.first){
          c[u[a.second][j]]+=c[a.second];
          k.push(make_pair(a.second,u[a.second][j]));
        }
      }
      k.pop();
    }
  }

  for(int i=0;i<n;i++){
    cout << c[i];
    if(i==n-1) cout << endl;
    else cout << " ";
  }
}
