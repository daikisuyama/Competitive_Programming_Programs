#include<iostream>
#include<vector>
#include<algorithm>
#include<utility>
#include<cmath>
using namespace std;
typedef long long ll;

const ll MAX = 200000;
const ll MOD=1000000007;
//マクロ
#define REP(i,n) for(ll i=0;i<(ll)(n);i++)
#define REPD(i,n) for(ll i=(ll)(n)-1;i>=0;i--)
#define FOR(i,a,b) for(ll i=(a);i<=(b);i++)
#define FORD(i,a,b) for(ll i=(a);i>=(b);i--)
#define ALL(x) (x).begin(),(x).end() //sortなどの引数を省略したい
#define SIZE(x) ((ll)(x).size()) //sizeをsize_tからllに直しておく
#define INF 1000000000000
#define PB push_back
#define MP make_pair
#define F first
#define S second

template<ll mod> class modint{
public:
    ll val=0;
    constexpr modint(ll x=0) noexcept : val(x%mod){
        while(x<0)x+=mod;
    }
    constexpr ll getmod(){return mod;}
    constexpr ll getvalue(){return val;}
    constexpr const ll &value() const noexcept {return val;}
    constexpr modint operator+(const modint &r) const noexcept{return modint(*this)+=r;}
    constexpr modint operator-(const modint &r) const noexcept{return modint(*this)-=r;}
    constexpr modint operator*(const modint &r) const noexcept{return modint(*this)*=r;}
    constexpr modint operator/(const modint &r) const noexcept{return modint(*this)/=r;}
    constexpr modint& operator+=(const modint &r) noexcept{
    val += r.val;
    if(val >= mod){
        val -= mod;
    }
    return *this;
    }
    constexpr modint& operator-=(const modint &r) noexcept{
    if(val < r.val){
        val += mod;
    }
    val -= r.val;
    return *this;
    }
    constexpr modint& operator*=(const modint &r) noexcept{
    val = val * r.val % mod;
    return *this;
    }
    constexpr modint& operator/=(const modint &r) noexcept{
    ll a=r.val,b=mod,u=1,v=0;
    while (b) {
        ll t = a/b;
        a -= t*b;swap(a,b);
        u -= t*v;swap(u,v);
    }
    val = val * u % mod;
    if(val < 0)val += mod;
    return *this;
    }
    constexpr bool operator == (const modint& r) const noexcept {
    return this->val == r.val;
    }
    constexpr bool operator < (const modint& r) const noexcept {
    return this->val < r.val;
    }
    constexpr bool operator != (const modint& r) const noexcept {
    return this->val != r.val;
    }
    friend constexpr ostream& operator << (ostream &os, const modint<mod>& x) noexcept {
    return os << x.val;
    }
    friend constexpr modint<mod> modpow(const modint<mod> &a,ll n) noexcept {
    if(n == 0) return 1;
    auto t = modpow(a, n / 2);
    t = t * t;
    if(n & 1) t = t * a;
    return t;
    }
};

using mint = modint<MOD>;

signed main(){
    ll n,a,b;cin >> n >> a >> b;
    const mint x=2;
    mint ans=modpow(x,n);//cout << 1 << endl;
    ans-=1;
    //cout << 1 << endl;
    vector<mint> com(b+1);
    FOR(i,1,b){
        if(i==1){
            com[i]=n;
        }else{
            com[i]=com[i-1];
            com[i]*=(n-i+1);
            com[i]/=i;
        }
    }
    ans=ans-com[a]-com[b];
    cout << ans << endl;
}