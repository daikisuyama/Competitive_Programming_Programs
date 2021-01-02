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
  return ll(x*y/gcd(x,y));
}

#endif

int main(){
  ll x,y;cin >> x >> y;
  cout << lcm(x,y) << endl;
}
