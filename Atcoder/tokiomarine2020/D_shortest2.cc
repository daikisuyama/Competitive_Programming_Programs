#include <bits/stdc++.h>
using namespace std;
int p[1024][1<<17],v[1<<19],w[1<<19],q,i,l;
int f(int a,int l){
    if(l<0)return -1e9;
    if(!a)return 0;
    if(a>1023)return max(f(a/2,l),f(a/2,l-w[a])+v[a]);
    if(~p[a][l])return p[a][l];
    return p[a][l]=max({f(a/2,l),f(a,l-1),f(a/2,l-w[a])+v[a]});
};
int main(){
    memset(p,-1,1<<29);
    cin>>l;
    for(;i++<l;)cin>>v[i]>>w[i];
    cin>>q;
    while(q--){cin>>i>>l;cout<<f(i,l)<<" ";}
}