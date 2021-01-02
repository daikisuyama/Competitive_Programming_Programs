#include<iostream>
using namespace std;
typedef long long ll;

const int MAX = 10000000;
//何で割るのか
const int MOD = 1000000007;

ll fac[MAX], finv[MAX], inv[MAX];

// テーブルを作る前処理
void COMinit() {
    fac[0] = fac[1] = 1;
    finv[0] = finv[1] = 1;
    inv[1] = 1;
    for (int i = 2; i < MAX; i++){
        fac[i] = fac[i - 1] * i % MOD;
        inv[i] = MOD - inv[MOD%i] * (MOD / i) % MOD;
        finv[i] = finv[i - 1] * inv[i] % MOD;
    }
}

// 二項係数計算
ll COM(int n, int k){
    if (n < k) return 0;
    if (n < 0 || k < 0) return 0;
    return fac[n] * (finv[k] * finv[n - k] % MOD) % MOD;
}

int main(){
  // 前処理
  COMinit();
  int n,m;cin >> n >> m;
  if(n-m==1 or n-m==-1){
    cout << ((fac[n]%MOD)*fac[m])%MOD << endl;
  }else if(n==m){
    cout << (((fac[n]%MOD)*fac[m])%MOD*2)%MOD << endl;
  }else{
    cout << 0 << endl;
  }
}
