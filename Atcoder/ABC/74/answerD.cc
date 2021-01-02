#include<iostream>
#include<vector>
#include<cmath>
using namespace std;
typedef long long ll;

signed main(){
  ll n;cin >> n;
  vector< vector<ll> > a(n,vector<ll>(n,0));
  vector< vector<ll> > b(n,vector<ll>(n,0));
  for(ll i=0;i<n;i++)for(ll j=0;j<n;j++) cin >> a[i][j];
  bool f=false;
  for(ll k=0;k<n;k++){
    for(ll i=0;i<n;i++){
      for(ll j=0;j<n;j++){
        if(a[i][j]>a[i][k]+a[k][j]){
          f=true;
        }else if(i!=j and i!=k and j!=k and a[i][j]==a[i][k]+a[k][j]){
          b[i][j]=1;
        }
      }
    }
  }
  if(f){
    cout << -1 << endl;
  }else{
    ll cnt=0;
    for(ll i=0;i<n;i++){
      for(ll j=0;j<n;j++){
        if(b[i][j]==0){
          cnt+=a[i][j];
        }
      }
    }
    //ここでミスった最悪
    //戻り値は整数型ではない
    cout << ll(cnt/2) << endl;
  }
}
