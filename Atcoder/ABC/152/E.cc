#include<iostream>
#include<vector>
#include<cmath>
#include<algorithm>
using namespace std;
typedef long long ll;

ll gcd(ll x,ll y){
  if(x<y) swap(x,y);
  //xの方が常に大きい
  while(y>0){
    ll r=x%y;
    x=y;
    y=r;
  }
  return x;
}

ll lcm(ll x,ll y){
  return ll(x*y/gcd(x,y));
}

//n個の場合のlcmも2個で比べて順に適用していくだけ
signed main(){
  ll inf=pow(10,9)+7;
  ll n;cin >> n;
  vector<ll> a(n);for(ll i=0;i<n;i++){cin >> a[i];}
  ll ans=lcm(a[0],a[1]);
  for(ll i=1;i<n;i++){ans=lcm(ans,a[i]);}
  //cout << ans << endl;
  ll cnt=0;
  for(ll i=0;i<n;i++){
    cnt+=ll(ans/a[i]);
    cnt%=inf;
  }
  cout << cnt << endl;
}
