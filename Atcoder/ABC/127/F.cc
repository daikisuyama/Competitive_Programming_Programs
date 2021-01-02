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

//multiset同じ奴が削除(普通にeraseだと)
//イテレータで範囲を指定すればいいだけ
signed main(){
    //入力の高速化用のコード
    //ios::sync_with_stdio(false);
    //cin.tie(nullptr);
    ll q;cin >> q;
    multiset<ll> A1,A2;
    ll B=0;
    ll s1,s2;s1=0;s2=0;
    ll l1,l2;l1=0;l2=0;
    REP(i,q){
        ll x,a,b;cin >> x;
        if(x==1){
            cin >> a >> b;
            B+=b;
            if(i==0){
                A1.insert(a);
                l1+=1;
                s1+=a;
            //l1=l2の時
            //l2で調べて一番前ならl1にいれる
            //そうでないならl2の最小をl1にいれる
            //先にA2に入れて最小をA1にいれる
            }else if((l1+l2)%2==0){
                s2+=a;
                A2.insert(a);
                ll j=*A2.begin();
                s1+=j;
                s2-=j;
                A1.insert(j);
                //A2.erase(j);
                A2.erase(A2.begin(),++A2.begin());
                l1+=1;
            //l1+1=l2の時
            //l1で調べて一番後ならl2にいれる
            //そうでないならl1の最大をl2にいれる
            //先にA1に入れて最大をA2にいれる
            }else{
                s1+=a;
                A1.insert(a);
                ll j=*(--A1.end());
                s2+=j;
                s1-=j;
                A2.insert(j);
                A1.erase(--A1.end(),A1.end());
                l2+=1;
            }
        }else{
            ll j=*(--A1.end());
            cout << j << " " << -s1+s2+j*(l1-l2)+B << endl;
        }
    }
}