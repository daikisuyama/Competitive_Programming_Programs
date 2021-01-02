//Codeforcesで128bit整数を使いたいとき
//→__int128_tを使う&GNU C++17 (64)で提出する

//インクルードなど
#include<numeric>
#include<vector>
#include<iostream>
using namespace std;
typedef long long ll;

//イテレーション
#define REP(i,n) for(ll i=0;i<ll(n);i++)
//aをbで割る時の繰上げ,繰り下げ
ll myceil(ll a,ll b){return (a+(b-1))/b;}
ll myfloor(ll a,ll b){return a/b;}

/*
二元一次不定方程式 ax+by=c(a≠0かつb≠0) を解く
初期化すると、x=x0+m*b,y=y0-m*aで一般解が求められる(m=0で初期化)
llは32bit整数まで→超えたらPythonに切り替え
*/
struct LDE{
    ll a,b,c,x,y;
    ll m=0;
    bool check=true;//解が存在するか

    //初期化
    LDE(ll a_,ll b_,ll c_): a(a_),b(b_),c(c_){
        ll g=gcd(a,b);
        if(c%g!=0){
            check=false;
        }else{
            //ax+by=gの特殊解を求める
            extgcd(abs(a),abs(b),x,y);
            if(a<0)x=-x;
            if(b<0)y=-y;
            //ax+by=cの特殊解を求める(オーバフローに注意！)
            x*=c/g;y*=c/g;
            //一般解を求めるために割る
            a/=g;b/=g; 
        }
    }

    //拡張ユークリッドの互除法
    //返り値:aとbの最大公約数
    ll extgcd(ll a,ll b,ll &x0,ll &y0){
        if(b==0){
            x0=1;
            y0=0;
            return a;
        }
        ll d=extgcd(b,a%b,y0,x0);
        y0-=a/b*x0;
        return d;
    }

    //パラメータmの更新(書き換え)
    void m_update(ll m_){
        x+=(m_-m)*b;
        y-=(m_-m)*a;
        m=m_;
    }
};

ll n,s,k,t,ch;
signed main(){
    cin>>t;
    REP(i,t){
        cin>>n>>s>>k;
        LDE sol=LDE(-k,n,s);
        if(!sol.check){
            cout<<-1<<endl;
            continue;
        }
        if(sol.y<0){
            ch=myceil(-sol.y,-sol.a);
        }else{
            ch=-myfloor(sol.y,-sol.a);
        }
        if(sol.x<0){
            ch=max(ch,myceil(-sol.x,sol.b));
        }else{
            ch=max(ch,-myfloor(sol.x,sol.b));
        }
        sol.m_update(ch);
        cout<<sol.x<<endl;
    }
}