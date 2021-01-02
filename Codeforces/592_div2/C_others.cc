#include<bits/stdc++.h>
using namespace std;
#pragma region atcoder
/*#include <atcoder/all>
using namespace atcoder;*/
//using mint = modint998244353;
//using mint = modint1000000007;
#pragma endregion
#pragma region macros
using ll = long long;
using pii = pair<int, int>;
using pll = pair<ll, ll>;
using vi = vector<int>;
using vs = vector<string>;
using vl = vector<ll>;
using vb = vector<bool>;
using vvi = vector<vector<int>>;
using vvl = vector<vector<ll>>;
#define rep(i, n) for(int i = 0; i < n; i++)
#define REP(i, a, b) for(int i = a; i < b; i++)
#define rrep(i, n) for(int i = n - 1; i >= 0; i--)
#define RREP(i, a, b) for(int i = b - 1; i >= a; i--)
#define all(x) (x).begin(), (x).end()
#define rall(x) (x).rbegin(), (r).rend()
#define sz(x) ((int)(x).size())
#define pb push_back
#define lb lower_bound
#define ub upper_bound
#define fi first
#define se second
#pragma endregion
#pragma region debug for var, v, vv
#define debug(var)  do{std::cout << #var << " : ";view(var);}while(0)
template<typename T> void view(T e){std::cout << e << std::endl;}
template<typename T> void view(const std::vector<T>& v){for(const auto& e : v){ std::cout << e << " "; } std::cout << std::endl;}
template<typename T> void view(const std::vector<std::vector<T> >& vv){cout << endl;int cnt = 0;for(const auto& v : vv){cout << cnt << "th : "; view(v); cnt++;} cout << endl;}
#pragma endregion
#pragma region int128
std::ostream &operator<<(std::ostream &dest, __int128_t value) {
  std::ostream::sentry s(dest);
  if (s) {
    __uint128_t tmp = value < 0 ? -value : value;
    char buffer[128];
    char *d = std::end(buffer);
    do {
      --d;
      *d = "0123456789"[tmp % 10];
      tmp /= 10;
    } while (tmp != 0);
    if (value < 0) {
      --d;
      *d = '-';
    }
    int len = std::end(buffer) - d;
    if (dest.rdbuf()->sputn(d, len) != len) {
      dest.setstate(std::ios_base::badbit);
    }
  }
  return dest;
}
#pragma endregion
const ll mod = 998244353;
const int inf = 1001001001;
const ll INF = 1001001001001001001;

int dx[4]={1,0,-1,0};
int dy[4]={0,1,0,-1};

template<class T>bool chmax(T &a, const T b) { if (a<b) { a=b; return 1; } return 0; }
template<class T>bool chmin(T &a, const T b) { if (b<a) { a=b; return 1; } return 0; }
ll rudiv(ll a, ll b) { return a/b+((a^b)>0&&a%b); } //  20 / 3 == 7
ll rddiv(ll a, ll b) { return a/b-((a^b)<0&&a%b); } // -20 / 3 == -7
ll power(ll a, ll p){ll ret = 1; while(p){if(p & 1){ret = ret * a;} a = a * a; p >>= 1;} return ret;}
ll modpow(ll a, ll p){ll ret = 1; while(p){if(p & 1){ret = ret * a % mod;} a = a * a % mod; p >>= 1;} return ret;}

/*--------------------------------------------------------------------------------------------------------------------------------*/
ll extGCD(long long a, long long b, __int128_t &x, __int128_t &y) {
    if (b == 0) {
        x = 1;
        y = 0;
        return a;
    }
    long long d = extGCD(b, a%b, y, x);
    y -= a/b * x;
    return d;
}
int main() {
	cin.tie(0);
	ios::sync_with_stdio(false);
	//cout << fixed << setprecision(15);
	ll n, p1 ,w, d; cin >> n >> p1 >> w >> d;
	// w * x + d * y = p1
	if(p1 % gcd(w, d) != 0) cout << -1 << endl, exit(0);
	__int128_t y1, x1;
	ll p = extGCD(w, d, x1, y1);
	ll a = w/p, b = d/p;
	ll mul =  p1 / p;
	y1 *= mul, x1 *= mul;
	ll x, y, z = -inf;
	__int128_t i = max((-x1) / b, (y1 - n) / a) - 2, j = min((n - x1) / b, y1 / a) + 2;
	/*debug(i);debug(j);debug(a); debug(b);debug(x1); debug(y1);
	debug(x1 + b * i + y1 - a * i);debug(x1 + b * j + y1 - a * j);*/
	if(x1 + b * i + y1 - a * i > n && x1 + b * j + y1 - a * j > n) cout << -1 << endl, exit(0);
    //change from here
	x = x1 + b * i, y = y1 - a * i;
	cout << x << " " << y << " " << z << endl;
	if(z == -inf) cout << -1 << endl;
} 
/*	
	* review you code when you get WA (typo? index?)
	* int overflow, array bounds
	* special cases (n=1?)
*/