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

//けんちょんさんの

const int MAX_V = 100000;  // ツリーのサイズのありうる最大値

int N;  // ツリーのサイズ
vector<vector<int>> tree;  // ツリーを隣接リスト形式のグラフ構造で表したもの

vector<int> sizeSubtree;  // sizeSubtree[v] := v を根とする部分ツリーのサイズ
vector<int> centroids;  // 重心列挙の答えがここに入る

/* ツリーDP */
void SubFindCentroids(int v, int parent_of_v = -1) {
    sizeSubtree[v] = 1;
    bool isCentroid = true;
    for (auto ch : tree[v]) {
        if (ch == parent_of_v) continue;
        SubFindCentroids(ch, v);
        if (sizeSubtree[ch] > N / 2) isCentroid = false;
        sizeSubtree[v] += sizeSubtree[ch];
    }
    if (N - sizeSubtree[v] > N / 2) isCentroid = false;
    if (isCentroid) centroids.push_back(v);
}

void FindCentroids() {
    centroids.clear();
    SubFindCentroids(0, N); // これを呼び出すと centoroids に重心を列挙したものが入る
}

vector<bool> check;
vector<ll> leaf;

void dfs(ll i){
    ll f=0;
    FORA(j,tree[i]){
        if(!check[j]){
            check[j]=true;
            dfs(j);
            f++;
        }
    }
    if(f==0)leaf.PB(i);
}

signed main(){
    ll t;cin>>t;
    REP(_,t){
        cin>>N;
        tree=vector<vector<int>>(N);
        sizeSubtree=vector<int>(N);
        centroids.clear();
        check=vector<bool>(N,false);
        leaf.clear();
        REP(i,N-1){
            ll x,y;cin>>x>>y;
            tree[x-1].PB(y-1);
            tree[y-1].PB(x-1);
        }
        FindCentroids();
        if(SIZE(centroids)==1){
            cout<<"1 "<<tree[0][0]+1<<endl;
            cout<<"1 "<<tree[0][0]+1<<endl;
            continue;
        }
        ll l,r;l=centroids[0];r=centroids[1];
        check[r]=true;check[l]=true;
        //lからdfs
        dfs(l);
        //葉を削除
        //leaf.erase(find(ALL(leaf),l));
        ll x=leaf[0];
        cout<<x+1<<" "<<tree[x][0]+1<<endl;
        if(SIZE(tree[r])==2){
            cout<<r+1<<" "<<x+1<<endl;
            continue;
        }
        FORA(i,tree[r]){
            if(i!=l){
                cout<<i+1<<" "<<x+1<<endl;
                break;
            }
        }
    }
}