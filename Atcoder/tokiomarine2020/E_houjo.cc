//インクルード(アルファベット順)
#include<algorithm>//sort,二分探索,など
#include<bitset>//固定長bit集合
#include<cmath>//pow,logなど
#include<complex>//複素数
#include<deque>//両端アクセスのキュー
#include<functional>//sortのgreater
#include<iomanip>//setprecision(浮動小数点の出力の誤差)
#include<iostream>//入出力
#include<iterator>//集合演算(積集合,和集合,差集合など)
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
//forループ関係
//引数は、(ループ内変数,動く範囲)か(ループ内変数,始めの数,終わりの数)、のどちらか
//Dがついてないものはループ変数は1ずつインクリメントされ、Dがついてるものはループ変数は1ずつデクリメントされる
#define REP(i,n) for(ll i=0;i<(ll)(n);i++)
#define REPD(i,n) for(ll i=n-1;i>=0;i--)
#define FOR(i,a,b) for(ll i=a;i<=(ll)(b);i++)
#define FORD(i,a,b) for(ll i=a;i>=(ll)(b);i--)
//xにはvectorなどのコンテナ
#define ALL(x) (x).begin(),(x).end() //sortなどの引数を省略したい
#define SIZE(x) ((ll)(x).size()) //sizeをsize_tからllに直しておく
//定数
#define INF 1000000000000 //10^12:極めて大きい値,∞
#define MOD 1000000007 //10^9+7:合同式の法
#define MAXR 100 //10^5:配列の最大のrange(素数列挙などで使用)
//略記
#define PB push_back //vectorヘの挿入
#define MP make_pair //pairのコンストラクタ
#define F first //pairの一つ目の要素
#define S second //pairの二つ目の要素

ll fac[MAXR+1],finv[MAXR+1],inv[MAXR+1];

//テーブルの作成
void COMinit() {
    fac[0]=fac[1]=1;
    finv[0]=finv[1]=1;
    inv[1]=1;
    FOR(i,2,MAXR){
        fac[i]=fac[i-1]*i%MOD;
        inv[i]=MOD-inv[MOD%i]*(MOD/i)%MOD;
        finv[i]=finv[i-1]*inv[i]%MOD;
    }
}

// 二項係数の計算
ll COM(ll n,ll k){
    if(n<k)return 0;
    if(n<0 || k<0)return 0;
    return fac[n]*(finv[k]*finv[n-k]%MOD)%MOD;
}


//無限ループかなあ？？？
signed main(){
    //これ書き忘れすぎ
    COMinit();
    //入力の高速化用のコード
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    ll n,k,s,t;cin >> n >> k >> s >> t;
    vector<ll> b(n);REP(i,n)cin >> b[i];
    vector<ll> a;
    //i bit目を見て、s_i=1,t_i=0の時はi bit目は全ての数が1,0でなければならないので
    REP(i,n){
        bool f=true;
        REP(j,18){
            if((s>>j)&1 and (t>>j)&1){
                if(!((b[i]>>j)&1)){
                    f=false;break;
                }
            }else if(!((s>>j)&1) and !((t>>j)&1)){
                if((b[i]>>j)&1){
                    f=false;break;
                }
            }else if((s>>j)&1 and !((t>>j)&1)){
                cout<<0<<endl;return 0;
            }
        }
        if(f)a.PB(b[i]);
    }
    n=SIZE(a);
    k=min(n,k);
    //以下ではそれぞれのbitは0と1が少なくとも一つなければならない
    //余事象を考えれば、1だけ0だけのbitが少なくとも一つあったらOK
    //それぞれのbitで"0になる集合"と"1になる集合"を用意すると、3^L(L=18)にならね？→O(N×3^L)
    //いや、分割してくだけか
    //チェックするのは結局N個くらいで済む→O(N×2^L)
    
    //まずは、それぞれのbitで集合を分割
    //全て異なるのでsetで良い
    vector<pair<unordered_set<ll>,unordered_set<ll>>> bits;
    REP(i,18){
        unordered_set<ll> f1,f2;
        REP(j,n){
            if((a[j]>>i)&1){
                f1.insert(a[j]);
            }else{
                f2.insert(a[j]);
            }
        }
        if(SIZE(f1) and SIZE(f2))bits.PB(MP(f1,f2));
    }
    ll bits_len=SIZE(bits);
    #if 0
    REP(i,bits_len){
        for(auto j=bits[i].F.begin();j!=bits[i].F.end();j++){
            cout << *j << " ";
        }
        cout << endl;
        for(auto j=bits[i].S.begin();j!=bits[i].S.end();j++){
            cout << *j << " ";
        }
        cout << endl;
    }
    #endif
    //集合分割したのでさらに分割を行う(部分集合全列挙→bit全探索)
    //全探索して全て数え上げたもの一旦ans_subに格納
    ll ans_sub=0;

    //ここで答えでの組み合わせの前計算しておく
    //prior_calc[j][i]：jC1+jC2+…+jCiの答え(j:1~n,i:1~k)
    vector<vector<ll>> prior_calc(n,vector<ll>(k,0));
    REP(j,n){
        prior_calc[j][0]=COM(j+1,1);
        FOR(i,1,k-1){
            prior_calc[j][i]=prior_calc[j][i-1]+COM(j+1,i+1);
        }
    }

    //2^L
    //使い回す
    deque<unordered_set<ll>> all_sets;
    FOR(i,1,(1<<bits_len)-1){
        //そこまでで分けられた集合を集合ごとに保存
        //deque<set<ll>> all_sets;
        all_sets.PB(unordered_set<ll>(ALL(a)));
        //L
        ll odd_even=0;
        REP(j,bits_len){
            if((i>>j)&1){
                odd_even+=1;
                ll s=SIZE(all_sets);
                //n
                REP(_,s){
                    //積集合をとりたい集合を書き出す
                    unordered_set<ll> ins=*(all_sets.begin());
                    all_sets.pop_front();
                    //一時保存用の集合を用意する
                    unordered_set<ll> f1,f2;
                    for(auto l=ins.begin();l!=ins.end();l++){
                        if(bits[j].F.find(*l)==bits[j].F.end()){
                            f1.insert(*l);
                        }else{
                            f2.insert(*l);
                        }
                    }
                    if(SIZE(f1)){all_sets.PB(f1);}
                    if(SIZE(f2)){all_sets.PB(f2);}
                }
            }
        }
        //これで完全に分割できた、あとはそれぞれの集合に対して1以上K以下の数を選ぶだけ
        ll s=SIZE(all_sets);
        //n
        REP(_,s){
            unordered_set<ll> now=*(all_sets.begin());
            all_sets.pop_front();
            ll s_sub=SIZE(now);
            //k→前計算で1にする
            if(odd_even%2){
                ans_sub+=prior_calc[s_sub-1][min(k,s_sub)-1];
            }else{
                ans_sub-=prior_calc[s_sub-1][min(k,s_sub)-1];
            }
        }
    }
    //cout << ans_sub << endl;
    ll ans=-ans_sub;
    FOR(i,1,k)ans+=COM(n,i);
    cout<< ans <<endl;
}