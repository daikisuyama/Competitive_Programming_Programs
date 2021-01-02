#include<iostream>
#include<vector>
#include<algorithm>
#include<cmath>
using namespace std;
typedef long long ll;

signed main(){
  ll n,d,a;cin >> n >> d >>a;
  vector<vector<ll>> xh(n,vector<ll>(2,0));
  vector<ll> x(n);
  vector<ll> h(n);
  for(ll i=0;i<n;i++){
    cin >> xh[i][0] >> xh[i][1];
  }
  sort(xh.begin(),xh.end());
  for(ll i=0;i<n;i++){
    x[i]=xh[i][0];h[i]=xh[i][1];
  }
  ll cnt=0;
  for(ll i=0;i<n;i++){
    if(h[i]>0){
      ll m=ll(ceil(h[i]/a));
      cnt+=m;
      ll k=upper_bound(x.begin()+i,x.end(),x[i]+2*d)-x.begin();
      ll g=m*a;
      for(ll j=i;j<k;j++){
        h[j]-=g;
      }
    }
  }
  cout << cnt << endl;
}
