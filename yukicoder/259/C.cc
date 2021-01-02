//コンパイラ最適化
#pragma GCC optimize("Ofast")
//インクルードなど
#include<bits/stdc++.h>
using namespace std;
typedef long long ll;

//マクロ
//forループ
//引数は、(ループ内変数,動く範囲)か(ループ内変数,始めの数,終わりの数)、のどちらか
//Dがついてないものはループ変数は1ずつインクリメントされ、Dがついてるものはループ変数は1ずつデクリメントされる
//FORAは範囲for文(使いにくかったら消す)
#define REP(i,n) for(ll i=0;i<ll(n);i++)
#define REPD(i,n) for(ll i=n-1;i>=0;i--)
#define FOR(i,a,b) for(ll i=a;i<=ll(b);i++)
#define FORD(i,a,b) for(ll i=a;i>=ll(b);i--)
#define FORA(i,I) for(const auto& i:I)
//xにはvectorなどのコンテナ
#define ALL(x) x.begin(),x.end() 
#define SIZE(x) ll(x.size()) 
//定数
#define INF 1000000000000 //10^12:∞
#define MOD 1000000007 //10^9+7:合同式の法
#define MAXR 100000 //10^5:配列の最大のrange
//略記
#define PB push_back //挿入
#define MP make_pair //pairのコンストラクタ
#define F first //pairの一つ目の要素
#define S second //pairの二つ目の要素

template<ll mod> class modint{
public:
    ll val=0;
    //コンストラクタ
    modint(ll x=0){while(x<0)x+=mod;val=x%mod;}
    //コピーコンストラクタ
    modint(const modint &r){val=r.val;}
    //算術演算子
    modint operator -(){return modint(-val);} //単項
    modint operator +(const modint &r){return modint(*this)+=r;}
    modint operator -(const modint &r){return modint(*this)-=r;}
    modint operator *(const modint &r){return modint(*this)*=r;}
    modint operator /(const modint &r){return modint(*this)/=r;}
    //代入演算子
    modint &operator +=(const modint &r){
        val+=r.val;
        if(val>=mod)val-=mod;
        return *this;
    }
    modint &operator -=(const modint &r){
        if(val<r.val)val+=mod;
        val-=r.val;
        return *this;
    }
    modint &operator *=(const modint &r){
        val=val*r.val%mod;
        return *this;
    }
    modint &operator /=(const modint &r){
        ll a=r.val,b=mod,u=1,v=0;
        while(b){
            ll t=a/b;
            a-=t*b;swap(a,b);
            u-=t*v;swap(u,v);
        }
        val=val*u%mod;
        if(val<0)val+=mod;
        return *this;
    }
    //等価比較演算子
    bool operator ==(const modint& r){return this->val==r.val;}
    bool operator <(const modint& r){return this->val<r.val;}
    bool operator !=(const modint& r){return this->val!=r.val;}
};

using mint = modint<MOD>;

//入出力ストリーム
istream &operator >>(istream &is,mint& x){//xにconst付けない
    ll t;is >> t;
    x=t;
    return (is);
}
ostream &operator <<(ostream &os,const mint& x){
    return os<<x.val;
}

//累乗
mint modpow(const mint &a,ll n){
    if(n==0)return 1;
    mint t=modpow(a,n/2);
    t=t*t;
    if(n&1)t=t*a;
    return t;
}



signed main(){
    //入力の高速化用のコード
    //ios::sync_with_stdio(false);
    //cin.tie(nullptr);
    ll h,w;cin>>h>>w;
    vector<vector<ll>> A(h,vector<ll>(w,0));
    REP(i,h)REP(j,w)cin>>A[i][j];
    vector<vector<vector<mint>>> s(4,vector<vector<mint>>(h+1,vector<mint>(w+1,1)));
    REP(j,h){
        REP(k,w){
            ll x,y;
            x=j;y=k;
            s[0][x+1][y+1]=s[0][x+1][y]*s[0][x][y+1]/s[0][x][y]*A[x][y];
        }
    }
    REP(j,h){
        REP(k,w-1){
            ll x,y;
            x=j;y=w-1-k;
            s[1][x+1][y-1]=s[1][x+1][y]*s[1][x][y-1]/s[1][x][y]*A[x][y];
        }
    }
    REP(j,h-1){
        REP(k,w){
            ll x,y;
            x=h-1-j;y=k;
            s[2][x-1][y+1]=s[2][x-1][y]*s[2][x][y+1]/s[2][x][y]*A[x][y];
        }
    }
    REP(j,h-1){
        REP(k,w-1){
            ll x,y;
            x=h-1-j;y=w-1-k;
            s[3][x-1][y-1]=s[3][x-1][y]*s[3][x][y-1]/s[3][x][y]*A[x][y];
        }
    }
    #if 0
    REP(i,4){
        REP(j,h){
            REP(k,w){
                cout<<s[i][j][k]<<" ";
            }
            cout<<endl;
        }
        cout<<endl;
    }
    #endif
    ll q;cin>>q;
    REP(_,q){
        ll r,c;cin>>r>>c;
        mint ans=1;
        ll x,y;
        x=r-1;y=c-1;
        ans*=s[0][x][y];
        //x=r;y=w-c;
        ans*=s[1][x][y];
        //x=h-r;y=c;
        ans*=s[2][x][y];
        //x=h-r;y=w-c;
        ans*=s[3][x][y];
        cout<<ans<<endl;
    }
}