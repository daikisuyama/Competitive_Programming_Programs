#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;
typedef long long ll;
#define INF 100000000000

signed main(){
  ll n,m,r;cin >> n >> m >> r;
  vector<ll> rx(r);for(int i=0;i<r;i++)cin >> rx[i];
  vector<vector<ll>> wf(n,vector<ll>(n,INF));
  for(int i=0;i<n;i++) wf[i][i]=0;
  for(int i=0;i<m;i++){
    ll a,b,c;cin >> a >> b >> c;
    wf[a-1][b-1]=c;
    wf[b-1][a-1]=c;
  }
  for(int k=0;k<n;k++){
    for(int i=0;i<n;i++){
      for(int j=0;j<n;j++){
        wf[i][j]=min(wf[i][j],wf[i][k]+wf[k][j]);
      }
    }
  }
  ll cnt=INF;
  vector<ll> v(r);for(int i=0;i<r;i++) v[i]=i;
  do{
    ll cnt_sub=0;
    for(int i=0;i<r-1;i++){
      cnt_sub+=wf[rx[v[i]]-1][rx[v[i+1]]-1];
    }
    cnt=min(cnt,cnt_sub);
  }while(next_permutation(v.begin(),v.end()));
  cout << cnt << endl;
}
