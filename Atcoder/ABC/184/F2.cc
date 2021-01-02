#include<iostream>
#include<algorithm>
#include<cstdlib>
#include<cstdint>
#define ll int_fast32_t
using namespace std;
ll a[45],suf[45],ans=0,n,t;
#pragma interrupt func
void func(){
	cout<<ans<<endl;
}

void dfs(ll k,ll sum) {
	if(k>n) return ;
    if(t-sum>ans){
        ans=t-sum;
    }else{
        if(t-sum+suf[k+1]<=ans) return ;
    }
	if(sum==0) {
		func();
		_Exit(0);
	}
	if(sum - a[k+1] >= 0) dfs(k+1,sum - a[k+1]);
	dfs(k+1,sum);
}

int main() {
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	cin>>n>>t;
	for(int i=1; i<=n; i++) cin>>a[i];
	sort(a+1,a+n+1,greater<>());
	for(int i=1; i<=n; i++){
		if(ans+a[i]<=t)ans+=a[i];
	}
	for(int i=n; i>=1; i--){
		suf[i]=suf[i+1]+a[i];
		if(suf[i]>t)suf[i]=t;
	}
	dfs(0,t);
	func();
	_Exit(0);
}