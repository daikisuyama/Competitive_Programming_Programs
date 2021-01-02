//比較関数
//https://qiita.com/a4rcvv/items/7cd217cc5fafef700dff
//int型では入りきらない場合もあるので注意する

#include<iostream>
#include<vector>
#include<utility>
#include<algorithm>
#include<cmath>
using namespace std;

typedef vector<pair<long long,long long> > food;

bool comp(const pair<long long,long long> &a,const pair<long long,long long> &b){
  return (a.first)*(a.second) > (b.first)*(b.second);
}

long long max(long long a,long long b){
  if(a>b){return a;}
  else{return b;}
}

long long min(long long a,long long b){
  if(a<b){return a;}
  else{return b;}
}


int main(){
  long long n,k;
  cin >> n >> k;
  vector<long long> v1(n,0);for(int i=0;i<n;i++){cin >> v1[i];}
  vector<long long> v2(n,0);for(int i=0;i<n;i++){cin >> v2[i];}
  food c(n,make_pair(0,0));
  sort(v1.begin(),v1.end());sort(v2.begin(),v2.end());
  reverse(v1.begin(),v1.end());
  for(int i=0;i<n;i++){
    c[i].first=v1[i];c[i].second=v2[i];
  }
  sort(c.begin(),c.end(),comp);
  if(n==1){
    cout << max(0,(c[0].first-k)*(c[0].second)) << endl;
  }else{
    while(k!=0 && c[0].first!=0){
      long long x=(c[0].first)*(c[0].second)-(c[1].first)*(c[1].second);
      if(x<c[0].second){
        k-=1;c[0].first-=1;
      }else{
        long long l=ceil(x/c[0].second);
        long long m=min(l,c[0].first);
        k-=m;c[0].first-=m;
      }
      for(food::iterator i=c.begin();i<c.end()-1;i++){
        if((i->first)*(i->second)<((i+1)->first)*((i+1)->second)){
          iter_swap(i,i+1);
        }else{
          break;
        }
      }
    }
    cout << (c[0].first)*(c[0].second) << endl;
  }

}
