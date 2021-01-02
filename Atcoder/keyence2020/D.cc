//同じものがあるとき間違える
#include<iostream>
#include<vector>
#include<algorithm>
#include<cmath>
#include<utility>
using namespace std;

signed main(){
  int n;cin >> n;
  vector<int> a(n);for(int i=0;i<n;i++) cin >> a[i];
  vector<int> b(n);for(int i=0;i<n;i++) cin >> b[i];
  int inf=10000000;
  int ans=inf;
  for(int i=0;i<(1<<n);i++){
    vector< vector<int> > x(n,vector<int>(3));
    for(int j=0;j<n;j++){
      if(i&(1<<j)){
        x[j][0]=a[j];x[j][1]=j;x[j][2]=0;
      }else{
        x[j][0]=b[j];x[j][1]=j;x[j][2]=1;
      }
    }
    vector< vector<int> > y(n,vector<int>(3));
    for(int j=0;j<n;j++){y[j]=x[j];}
    sort(x.begin(),x.end());
    bool f=true;
    //ありうる場合も除いてしまう
    for(int j=0;j<n;j++){
      if(abs(x[j][1]-j)%2!=x[j][2]){f=false;break;}
    }
    if(f){
      //ここ工夫する
      int c=0;
      for(int j=0;j<n-1;j++){
        for(int k=n-1;k>=j+1;k--){
          if(y[k]<y[k-1]){iter_swap(y.begin()+k,y.begin()+k-1);c+=1;}
          if(c==ans)break;
        }
        if(c==ans)break;
      }
      ans=c;
    }
  }
  if(ans==inf){
    cout << -1 << endl;
  }else{
    cout << ans << endl;
  }
}
