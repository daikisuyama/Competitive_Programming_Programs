#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;
typedef long long ll;

signed main(){
  ll h,n;cin >> h >> n;
  vector<ll> a(n);
  vector<ll> b(n);
  for(ll i=0;i<n;i++){
    cin >> a[i] >> b[i];
  }
  ll inf=10000000000;
  ll ma=*max_element(a.begin(),a.end());
  vector<ll> dp(h+1+ma,inf);dp[0]=0;
  for(ll i=0;i<n;i++){
    for(ll j=0;j<h+1+ma;j++){
      if(dp[j]!=inf){
        if(j+a[i]<=h+ma){
          dp[j+a[i]]=min(dp[j+a[i]],dp[j]+b[i]);
        }else{
          break;
        }
      }
    }
  }
  cout << *min_element(dp.begin()+h,dp.end()) << endl;
}
