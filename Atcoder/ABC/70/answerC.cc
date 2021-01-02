#include<iostream>
#include<vector>
#include<cmath>
#include<algorithm>
using namespace std;
typedef long long ll;

#if 1
//whileで小さくしてく
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

#endif

#if 1

ll lcm(ll x,ll y){
  //かけるで大きくなりすぎる
  return ll(x/gcd(x,y))*y;
}

#endif

int main(){
  ll n;cin >> n;
  ll ans=1;
  for(int i=0;i<n;i++){
    //cout << ans << endl;
    ll t;cin >> t;
    ans=lcm(ans,t);
  }
  cout << ans << endl;
}
