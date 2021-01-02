#include<iostream>
#include<vector>
#include<set>
#include<algorithm>
using namespace std;

int main(){
  int n,m;cin >> n >> m;
  vector<int> x;
  bool f=false;
  for(int i=0;i<m;i++){
    int a,b;cin >> a >>b;
    if(a==1){
      x.push_back(b);
    }
    if(b==n){
      x.push_back(a);
    }
  }
  int l1=x.size();
  set<int> y(x.begin(),x.end());
  if(l1==y.size()){
    cout << "IMPOSSIBLE" << endl;
  }else{
    cout << "POSSIBLE" << endl;
  }

}
