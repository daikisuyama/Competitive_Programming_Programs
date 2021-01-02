#include<iostream>
#include<vector>

using namespace std;
typedef vector< vector<int> > vv;
#define INF 10000000

void dfs(int now,vv& tree,vector<int>& dep,int d,vector<bool>& check){
  dep[now]=d;
  check[now]=true;
  int l=tree[now].size();
  for(int i=0;i<l;i++){
    if(check[tree[now][i]]==false){dfs(tree[now][i],tree,dep,d+1,check);}
  }
}

int main(){
  int n;cin >> n;
  vv tree(n);
  for(int i=0;i<n-1;i++){
    int a,b;cin >> a >> b;
    tree[a-1].push_back(b-1);
    tree[b-1].push_back(a-1);
  }
  vector<int> dep1(n,INF);
  vector<bool> check1(n,false);
  vector<int> dep2(n,INF);
  vector<bool> check2(n,false);
  dfs(0,tree,dep1,0,check1);
  dfs(n-1,tree,dep2,0,check2);
  int c1=0;int c2=0;
  for(int i=0;i<n;i++){
    if(dep1[i]<=dep2[i]){
      c1+=1;
    }else{
      c2+=1;
    }
  }
  if(c1>c2){
    cout << "Fennec" << endl;
  }else{
    cout << "Snuke" << endl;
  }
}
