#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

const int N = 200000;

vector<bool> isp(N+1, true);

void sieve() {
  isp[0] = false;
  isp[1] = false;
  for (int i=2; pow(i,2)<=N; i++) {
    if (isp[i]) for(int j=2; i*j<=N; j++) isp[i*j] = false;
  }
}

int main() {
  // N以下の整数に対して素数判定をしてくれます。
  // nが素数ならば isp(n)=true、そうでなければ isp(n)=false
  int n;cin >>n;
  sieve();
  // ex. 51から80までの素数を出力
  for (int i=n; i<=200000; i++){
    if(isp[i]){cout << i << endl;break;}
  }
  return 0;
}
