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
#define MAX(x) *max_element(ALL(x)) //最大値を求める
#define MIN(x) *min_element(ALL(x)) //最小値を求める
//定数
#define INF 1000000000000 //10^12:極めて大きい値,∞
#define MOD 1000000007 //10^9+7:合同式の法
#define MAXR 100000 //10^5:配列の最大のrange(素数列挙などで使用)
//略記
#define PB push_back //vectorヘの挿入
#define MP make_pair //pairのコンストラクタ
#define F first //pairの一つ目の要素
#define S second //pairの二つ目の要素


signed main(){
    //入力の高速化用のコード
    //ios::sync_with_stdio(false);
    //cin.tie(nullptr);
    ll f=2*pow(10,5);
    ll n,q;cin >> n >> q;
    vector<multiset<pair<ll,ll>>> youtien(f);
    vector<ll> doko(n);
    vector<ll> tikara(n);
    REP(i,n){
        ll a,b;cin >> a >> b;b--;
        youtien[b].insert(MP(a,i));
        doko[i]=b;
        tikara[i]=a;
    }
    multiset<pair<ll,ll>> youjitati;
    REP(i,f){
        if(!(youtien[i].empty())){
            youjitati.insert(*(--youtien[i].end()));
        }
    }
    
    REP(i,q){
        ll c,d;cin >> c >> d;c--;d--;
        if(youtien[d].size()>0 and youtien[doko[c]].size()>1){
            youjitati.erase(*(--youtien[d].end()));
            youjitati.erase(*(--youtien[doko[c]].end()));
            youtien[d].insert(MP(tikara[c],c));
            youtien[doko[c]].erase(MP(tikara[c],c));
            youjitati.insert(*(--youtien[d].end()));
            youjitati.insert(*(--youtien[doko[c]].end()));
            doko[c]=d;
        }else if(youtien[d].size()==0 and youtien[doko[c]].size()>1){
            youjitati.erase(*(--youtien[doko[c]].end()));
            youtien[d].insert(MP(tikara[c],c));
            youtien[doko[c]].erase(MP(tikara[c],c));
            youjitati.insert(*(--youtien[d].end()));
            youjitati.insert(*(--youtien[doko[c]].end()));
            doko[c]=d;
        }else if(youtien[d].size()>0 and youtien[doko[c]].size()==1){
            youjitati.erase(*(--youtien[doko[c]].end()));
            youjitati.erase(*(--youtien[d].end()));
            youtien[d].insert(MP(tikara[c],c));
            youtien[doko[c]].erase(MP(tikara[c],c));
            youjitati.insert(*(--youtien[d].end()));
            doko[c]=d;
        }else{
            youjitati.erase(*(--youtien[doko[c]].end()));
            youtien[d].insert(MP(tikara[c],c));
            youtien[doko[c]].erase(MP(tikara[c],c));
            youjitati.insert(*(--youtien[d].end()));
            doko[c]=d;
        }
        
        cout << (youjitati.begin())->F << endl;
    }
}