#include<iostream>
#include<vector>
#include<string>

using namespace std;
typedef vector< vector<int> > vv;
#define INF 1e9

void go_next(int I,int J,vv& dp,vector<string> x,int w,int h){
  if(I<h-1){
    if(x[I+1][J]=='.' and dp[I+1][J]>dp[I][J]+1){
      dp[I+1][J]=dp[I][J]+1;go_next(I+1,J,dp,x,w,h);
    }
  }
  if(0<I){
    if(x[I-1][J]=='.' and dp[I-1][J]>dp[I][J]+1){
      dp[I-1][J]=dp[I][J]+1;go_next(I-1,J,dp,x,w,h);
    }
  }
  if(J<w-1){
    if(x[I][J+1]=='.' and dp[I][J+1]>dp[I][J]+1){
      dp[I][J+1]=dp[I][J]+1;go_next(I,J+1,dp,x,w,h);
    }
  }
  if(0<J){
    if(x[I][J-1]=='.' and dp[I][J-1]>dp[I][J]+1){
      dp[I][J-1]=dp[I][J]+1;go_next(I,J-1,dp,x,w,h);
    }
  }
}

int main(){
  int h ,w;cin >> h >> w;
  vv dp(h,vector<int>(w,INF));dp[0][0]=1;
  vector<string> x(h);for(int i=0;i<h;i++)cin >>x[i];
  int c=0;
  for(int i=0;i<h;i++){
    for(int j=0;j<w;j++){
      if(x[i][j]=='.'){c+=1;}
    }
  }
  go_next(0,0,dp,x,w,h);
  if(dp[h-1][w-1]==INF)cout << -1 << endl;
  else cout << c-dp[h-1][w-1] << endl;
}
