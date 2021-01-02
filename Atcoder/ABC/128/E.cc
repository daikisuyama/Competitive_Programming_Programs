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
#define ALL(x) x.begin(),x.end() //sortなどの引数を省略したい
#define SIZE(x) ll(x.size()) //sizeをsize_tからllに直しておく
//定数
#define INF 1000000000000 //10^12:極めて大きい値,∞
#define MOD 1000000007 //10^9+7:合同式の法
#define MAXR 100000 //10^5:配列の最大のrange(素数列挙などで使用)
//略記
#define PB push_back //vectorヘの挿入
#define MP make_pair //pairのコンストラクタ
#define F first //pairの一つ目の要素
#define S second //pairの二つ目の要素
#define Umap unordered_map
#define Uset unordered_set

//最後のところの処理がいい加減になっていた、こういう詰めの甘い実装がダメなんだよカス
signed main(){
    //入力の高速化用のコード
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    ll n,q;cin>>n>>q;

    vector<vector<ll>> xst(n);
    REP(i,n){
        ll s,t,x;cin>>s>>t>>x;
        xst[i]={x,s,t};
    }
    sort(ALL(xst));

    vector<ll> d(q);
    REP(i,q)cin>>d[i];

    vector<deque<ll>> ans_sectl(q);
    vector<deque<ll>> ans_sectr(q);
    REP(i,n){
        ll s,t,x;x=xst[i][0];s=xst[i][1];t=xst[i][2];
        ll L=(lower_bound(ALL(d),s-x)-d.begin());
        ll R=(upper_bound(ALL(d),t-x-1)-d.begin())-1;
        //lower,upper気を付ける
        //2RE
        if(L!=q and R!=-1){ans_sectl[L].PB(i);ans_sectr[R].PB(i);}
        //cout << L << " " << R << endl;
    }

    //複数存在する場合もあるので、map
    map<ll,ll> ans;
    REP(i,q){
        ll sl=SIZE(ans_sectl[i]);
        ll sr=SIZE(ans_sectr[i]);
        REP(_,sl){
            ans[*(ans_sectl[i].begin())]+=1;
            ans_sectl[i].pop_front();
        }
        //削除しておく
        while(!ans.empty()){
            if(ans.begin()->S==0){
                ans.erase(ans.begin());
            }else{
                break;
            }
        }
        if(ans.empty()){
            cout<<-1<<"\n";
        }else{
            cout<<xst[ans.begin()->F][0]<<"\n";
        }
        #if 0
        if(i==q-1){
            for(auto& e:ans)cout<<xst[e.F][0]<<endl;
        }
        #endif
        REP(_,sr){
            ans[*(ans_sectr[i].begin())]-=1;
            ans_sectr[i].pop_front();
        }
    }
}