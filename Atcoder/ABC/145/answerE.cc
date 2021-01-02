#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

int main(){
  int n,t;cin>>n>>t;
  vector< vector<int> > ab(n,vector<int>(2,0));
  for(int i=0;i<n;i++)cin >> ab[i][0] >> ab[i][1];
  sort(ab.begin(),ab.end(),[](const vector<int>& a,const vector<int>& b){return a[0]<b[0];});
  int m= ab[n-1][0];
  vector<int> dp(t+m);

  for(int i=0;i<n;i++){
    vector<int> dp_sub(t+m);
    for(int j=0;j<t;j++){
      if(j==0){dp_sub[ab[i][0]]=ab[i][1];}
      else if(dp[j]!=0){dp_sub[j+ab[i][0]]=dp[j]+ab[i][1];}
    }
    for(int j=0;j<t+m;j++){
      dp[j]=max(dp[j],dp_sub[j]);
    }
  }
  cout << *max_element(dp.begin(),dp.end()) << endl;
}
