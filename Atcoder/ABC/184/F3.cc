#pragma GCC optimize ("O2")
#include <cstdio>
#include <algorithm>
using namespace std;

int_fast8_t n;
int_fast32_t a[42], t, suf[42], ans = 0;

void dfs(const int_fast8_t& k, const int_fast32_t& sum) {
	if (k > n) return;
	if (t - sum > ans) ans = t - sum;
	else if(t - sum + suf[k + 1] <= ans) return;
	if (sum == 0) {
		printf("%d", t);
		exit(0);
	}
	if (sum >= a[k + 1]) dfs(k + 1, sum - a[k + 1]);
	dfs(k + 1, sum);
}

int main() {
	scanf("%d %d", &n, &t);
	for(int_fast8_t i = 1; i <= n; ++i) scanf("%d", &a[i]);
	sort(a + 1, a + n + 1, [](const int_fast32_t& x, const int_fast32_t& y){return x > y;});
	for(int_fast8_t i = n; i >= 1; --i){
      suf[i] = suf[i + 1] + a[i];
      if(suf[i]>t)suf[i]=t;
    }
	dfs(0, t);
	printf("%d", ans);
}