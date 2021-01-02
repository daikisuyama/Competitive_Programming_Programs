#include <bits/stdc++.h>
#include <boost/multiprecision/cpp_int.hpp>
using namespace std;
namespace mp = boost::multiprecision;
typedef mp::cpp_int ll;
 
const ll mod = 1000000007;
 
int main() {
    string N;
    cin >> N;
    int n = N.length();
    ll a[n + 1]{}, b[n + 1]{};
    a[0] = 1;
    ll ans = 0;
    for (int i = 0; i < n; i++) {
        a[i + 1] = (a[i] * 10) ;
        b[i + 1] = (b[i] + (i + 1) * a[i]) ;
    }
    for (ll i = 1; i <= n; i++) {
        ll c = N[i - 1] - '0';
        ll f = (((i - 1) * i) / 2);
        ans = (ans + c * f * a[n - i] + c * b[n - i]);
    }
    cout << ans << "\n";
    return 0;
}
