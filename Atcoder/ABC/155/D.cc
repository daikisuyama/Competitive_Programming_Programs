#include<algorithm>//sort,二分探索,など
#include<bitset>//固定長bit集合
#include<cmath>//pow,logなど
#include<complex>//複素数
#include<deque>//両端アクセスのキュー
#include<functional>//sortのgreater
#include<iomanip>//setprecision(浮動小数点の出力の誤差)
#include<iostream>//入出力
#include<map>//map(辞書)
#include<numeric>//iota(整数列の生成),gcdとlcm(c++17)
#include<queue>//キュー
#include<set>//集合
#include<stack>//スタック
#include<string>//文字列
#include<unordered_map>//イテレータあるけど順序保持しないmap
#include<unordered_set>//イテレータあるけど順序保持しないset
#include<utility>//pair
#include<vector>//可変長配列

using namespace std;
typedef long long ll;

//マクロ
#define REP(i,n) for(ll i=0;i<(ll)(n);i++)
#define REPD(i,n) for(ll i=(ll)(n)-1;i>=0;i--)
#define FOR(i,a,b) for(ll i=(a);i<=(b);i++)
#define FORD(i,a,b) for(ll i=(a);i>=(b);i--)
#define ALL(x) (x).begin(),(x).end() //sortなどの引数を省略したい
#define SIZE(x) ((ll)(x).size()) //sizeをsize_tからllに直しておく
#define INF 1000000000000
#define MOD 10000007
#define PB push_back
#define MP make_pair
#define F first
#define S second

ll l1,l2,l3;

ll countk1(ll x,vector<ll> b11,vector<ll> b13){
    ll ret=0;
    REP(i,l1){
        ll lx=0;ll rx=l3-1;
        while(lx+1<rx){
            ll t=(lx+rx)/2;
            if(b13[t]*b11[i]<=x){lx=t;}else{rx=t;}
        }
        if(b13[rx]*b11[i]<=x){
            ret+=(rx+1);
        }else if(b13[lx]*b11[i]<=x){
            ret+=(lx+1);
        }
    }
    return ret;
}

ll countk2(ll x,vector<ll> b21,vector<ll> b23){
    ll ret=0;
    REP(i,l1-1){
        ll lx=i+1;ll rx=l1-1;
        while(lx+1<rx){
            ll t=(lx+rx)/2;
            if(b21[t]*b21[i]<=x){lx=t;}else{rx=t;}
        }
        if(b21[rx]*b21[i]<=x){
            ret+=(rx-i);
        }else if(b21[lx]*b21[i]<=x){
            ret+=(lx-i);
        }
    }
    REP(i,l3-1){
        ll lx=i+1;ll rx=l3-1;
        while(lx+1<rx){
            ll t=(lx+rx)/2;
            if(b23[t]*b23[i]<=x){lx=t;}else{rx=t;}
        }
        if(b23[rx]*b23[i]<=x){
            ret+=(rx-i);
        }else if(b23[lx]*b23[i]<=x){
            ret+=(lx-i);
        }
    }
    return ret;
}

signed main(){
    ll n,k;cin >> n >> k;
    vector<ll> b1,b2,b3;
    REP(i,n){
        ll x;cin >> x;
        if(x<0){b1.PB(x);}else if(x==0){b2.PB(x);}else{b3.PB(x);}
    }
    l1=b1.size();l2=b2.size();l3=b3.size();
    sort(ALL(b1));sort(ALL(b3),greater<ll>());
    if(k<=l1*l3){
        ll l=b1[0]*b3[0];ll r=-1;
        while(l+1<r){
            ll t=(l+r)/2;
            if(countk1(t,b1,b3)>=k){r=t;}else{l=t;}
        }
        if(countk1(l,b1,b3)==k){
            cout << l << endl;
        }else{
            cout << r << endl;
        }
    }else if(k<=l1*l3+l2*(l1+l3)+(l2*(l2-1))/2){
        cout << 0 << endl;
    }else{
        k-=(l1*l3+l2*(l1+l3)+(l2*(l2-1))/2);
        ll l=1;ll r;
        if(l1>=2 and l3<2){
            r=b1[0]*b1[1];
        }else if(l1<2 and l3>=2){
            r=b3[0]*b3[1];
        }else{
            r=max(b1[0]*b1[1],b3[0]*b3[1]);
        }
        sort(ALL(b3));sort(ALL(b1),greater<ll>());

        while(l+1<r){
            ll t=(l+r)/2;
            if(countk2(t,b1,b3)>=k){r=t;}else{l=t;}
        }
        
        if(countk2(l,b1,b3)==k){
            cout << l << endl;
        }else{
            cout << r << endl;
        }
    }
}