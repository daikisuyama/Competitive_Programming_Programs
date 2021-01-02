#include<iostream>
#include<vector>
#include<cmath>
#include<queue>

using namespace std;
#define MAX 150000
int sieve[MAX+1]={0};//i番目が整数iに対応(1~100000)
//エラトステネスの篩を実装する
void es(){
  //0のところは素数
  for(int i=2;i<=1000;i++){
    if(sieve[i]==0){
      for(int j=1;j<=floor(MAX/i);j++){
        if(j!=1) sieve[j*i]=1;
      }
    }
  }
}


int main(){
  es();
  int k;cin >> k;
  for(int i=k;i<=100010;i++){
    if(sieve[i]==0){cout << i << endl;break;}
  }
}
