#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
int main() {
  int n=4;
  vector<int> v(n);
  iota(v.begin(), v.end(), 0);
  do{
    //vは次の順列になる
    for(int i=0;i<n;i++){
          //なんらかの操作
    }
  }while(next_permutation(v.begin(),v.end()));
}
