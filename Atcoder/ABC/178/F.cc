//デバッグ用オプション：-fsanitize=undefined,address

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

signed main(){
    //入力の高速化用のコード
    //ios::sync_with_stdio(false);
    //cin.tie(nullptr);
    ll n;cin>>n;
    vector<ll> a(n);REP(i,n)cin>>a[i];
    vector<ll> b(n);REP(i,n)cin>>b[i];
    map<ll,ll> c;REP(i,n)c[b[i]]++;
    set<pair<ll,ll>> b_check;
    vector<ll> ans(n,-1);
    FORA(i,c){
        b_check.insert(MP(-i.S,i.F));
    }
    map<ll,deque<ll>> a_ind;REP(i,n)a_ind[a[i]].PB(i);
    set<pair<ll,ll>> a_left;
    //逆順なので-に
    FORA(i,a_ind){
        a_left.insert(MP(-SIZE(i.S),i.F));
    }
    FORA(i,b_check){
        //cout<<1<<endl;
        ll now,now_num;now=-i.F;now_num=i.S;
        //範囲for文だと壊れる
        auto j=a_left.begin();
        while(j!=a_left.end()){
            if(j->S==now_num){
                FORA(i,a_ind[j->S]){
                    others.PB(j->S);
                }
                j=a_left.erase(j);
                continue;
            }
            if((-j->F)>now){
                //cout<<1<<endl;
                //cout<<now<<endl;
                REP(k,now){
                    ans[a_ind[j->S].front()]=now_num;
                    //cout<<a_ind[j->S][(-j->F)-k]<<" "<<now_num<<endl;
                    //cout<<5<<endl;
                    a_ind[j->S].pop_front();
                }
                pair<ll,ll> ne=*j;
                ne.F+=now;
                //cout<<ne.F<<" "<<ne.S<<endl;
                a_left.erase(j);
                a_left.insert(ne);
                break;
            }else{
                FORA(k,a_ind[j->S]){
                    ans[k]=now_num;
                    //cout<<k<<endl;
                }
                now-=(-j->F);
                j=a_left.erase(j);
            }
        }
    }
    REP(i,n){
        if(ans[i]==-1 and SIZE(others)>0){
            ans[i]=others.front();
            others.pop_front();
        }
    }
    REP(i,n){
        if(ans[i]==-1){
            cout<<"No"<<endl;
            return 0;
        }
    }
    cout<<"Yes"<<endl;
    REP(i,n){
        if(i!=n-1){cout<<ans[i]<<" ";}
        else{cout<<ans[i]<<endl;}
    }


}