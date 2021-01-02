#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

int main(){
  int n;
  int lx;
  int a,b,c;
  vector<int> l;
  int x;
  int co=0;
  cin>>n;
  for(int i=0;i<n;i++){
    cin >> lx;
    l.push_back(lx);
  }
  sort(l.begin(),l.end());
  reverse(l.begin(),l.end());
  for(int i=0;i<n-2;i++){
    c=l[i];
    x=0;
    for(int j=i+1;j<n-1;j++){
      b=l[j];
      for(int k=j+1;k<n;k++){
        a=l[k];
        if(c<(a+b)){
          co+=1;
        }else{
          if(k==j+1){x=1;}
          break;
        }
      }
      if(x==1){break;}
    }
  }
  cout << co << endl;
}
