#include<iostream>
#include<vector>
#include<algorithm>
#include<cmath>
using namespace std;
typedef long long ll;
ll x,y,z,k;

ll unti(ll t_sub,vector<ll> ab_max,vector<ll> c){
  ll ret=0;
  for(ll i=0;i<x*y;i++){
    ll h=z-(*lower_bound(c.begin(),c.end(),t_sub-ab_max[i]));
    if(h==0 or ret>=k) return ret;
    else ret+= h;
  }
  return ret;
}

signed main(){
  cin >> x >> y >> z >> k;
  vector<ll> a(x);vector<ll> b(y);vector<ll> c(z);
  for(ll i=0;i<x;i++) cin >> a[i];
  for(ll i=0;i<y;i++) cin >> b[i];
  for(ll i=0;i<z;i++) cin >> c[i];
  sort(c.begin(),c.end());
  vector<ll> ab_max(x*y);
  for(ll i=0;i<x;i++)
    for(ll j=0;j<y;j++)
      ab_max[i*y+j]=(a[i]+b[j]);
  ll l=0;ll r=ab_max[0]+c[z-1];
  while(r>l+1){
    ll t=floor((l+r)/2);
    if(unti(t,ab_max,c)>=k) r=t;
    else l=t;
  }
  vector<ll> ans;
  bool f=false;
  for(ll i=0;i<x*y;i++){
    for(ll j=z-1;j>-1;j--){
      ll u=ab_max[i]+c[j];
      if(u>=r){
        ans.push_back(u);
      }else{
        if(j==0) f=true;
        break;
      }
    }
    if(f) break;
  }
  sort(ans.begin(),ans.end(),greater<ll>());
  for(ll i=0;i<k;i++){
    cout << ans[i] << endl;
  }
}
