#pragma GCC optimize("Ofast")
#include<iostream>
#include<algorithm>
#include<deque>
#include<utility>
using namespace std;
typedef long long ll;
ll a[45],suf[45],ans=0,n,t,v,w;
deque<pair<ll,ll>> d;

inline bool cmp(int x,int y) {
	return x>y;
}
int main(){
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);
    cout.tie(nullptr);
	cin>>n>>t;
	for(int i=1;i<=n;++i){
        cin>>a[i];
    }
	stable_sort(a+1,a+n+1,cmp);
	for(int i=n;i>=1;--i){
        suf[i]=suf[i+1]+a[i];
    }
    d.emplace_back(0,t);
    while(!d.empty()){
        v=d.front().first;w=d.front().second;d.pop_front();
        if(v>n)continue;
        if(t-w>ans){
            ans=t-w;
        }else{
            if(t-w+suf[v+1]<=ans)continue;
        }
        if(ans==t){
            cout<<ans;
            return 0;
        }
        if(w-a[v+1]>=0)d.emplace_front(v+1,w-a[v+1]);
	    d.emplace_front(v+1,w);
    }
	cout<<ans;
	return 0;
}