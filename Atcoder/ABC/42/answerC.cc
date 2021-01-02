#include<iostream>
#include<vector>
#include<algorithm>
#include<utility>
#include<cmath>
using namespace std;
typedef long long ll;

const ll MAX = 200000;
const ll MOD = 1000000007;

ll fac[MAX], finv[MAX], inv[MAX];

// テーブルを作る前処理
void COMinit() {
    fac[0] = fac[1] = 1;
    finv[0] = finv[1] = 1;
    inv[1] = 1;
    for (ll i = 2; i < MAX; i++){
        fac[i] = fac[i - 1] * i % MOD;
        inv[i] = MOD - inv[MOD%i] * (MOD / i) % MOD;
        finv[i] = finv[i - 1] * inv[i] % MOD;
    }
}

// 二項係数計算
ll COM(ll n,ll k){
    if (n < k) return 0;
    if (n < 0 || k < 0) return 0;
    return fac[n] * (finv[k] * finv[n - k] % MOD) % MOD;
}

signed main(){
  // 前処理
  COMinit();
  ll h,w,a,b;cin >> h >> w >> a >> b;
  ll ans=COM(h+w-2,h-1);//cout << ans << endl;
  ll m=min(a,b);
  for(int i=0;i<m;i++){
    //cout << 1 << endl;
    ll ans_sub=COM(h-a+b-1,b-i-1)*COM(w-b+a-1,a-i-1)%MOD;
    ans-=ans_sub;
    if(ans<0){
      ans+=MOD;
      //cout << 1 << endl;
    }
  }
  cout << ans << endl;
}
