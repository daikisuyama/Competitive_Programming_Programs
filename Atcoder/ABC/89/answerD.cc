#include<iostream>
#include<vector>
#include<utility>
#include<cmath>

using namespace std;
typedef vector< vector<int> > vv;
typedef vector< vector< pair<int,int> > > vvp;

int make_distance(pair<int,int>& S,pair<int,int>& T){
  return abs(S.first-T.first)+abs(S.second-T.second);
}

int main(){

  int h,w,d;cin >> h >> w >> d;
  vv a(h,vector<int>(w,0));
  for(int i=0;i<h;i++){
    for(int j=0;j<w;j++){cin >> a[i][j];}
  }
  
  vv x1;
  vvp x2;
  for(int i=1;i<d+1;i++){
    int l=int((h*w-i)/d);
    vector<int> v1(l+1,0); vector< pair<int,int> > v2(l+1);
    x1.push_back(v1);x2.push_back(v2);
  }

  for(int i=0;i<h;i++){
    for(int j=0;j<w;j++){
      int p=a[i][j]%d;if(p==0){p=d-1;}else{p-=1;}
      int l=int((a[i][j]-(p+1))/d);
      x2[p][l]=make_pair(i,j);
    }
  }

  for(int i=1;i<d+1;i++){
    int l=int(x1[i-1].size());
    for(int j=0;j<l-1;j++){
      x1[i-1][j+1]=x1[i-1][j]+make_distance(x2[i-1][j],x2[i-1][j+1]);
    }
  }

  int q;cin >> q;
  for(int i=0;i<q;i++){
    int l,r;cin >> l >> r;
    int p=l%d;
    if(p==0){
      cout << x1[d-1][int(r/d)-1]-x1[d-1][int(l/d)-1] << endl;
    }else{
      cout << x1[p-1][int(r/d)]-x1[p-1][int(l/d)] << endl;
    }
  }

}
