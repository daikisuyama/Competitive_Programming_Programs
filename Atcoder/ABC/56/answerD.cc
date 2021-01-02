#include<iostream>
#include<vector>
#include<algorithm>
#include<cmath>

using namespace std;
typedef long long ll;
ll n,k;
vector<ll> a;

bool check(ll d){
    vector<ll> dp(k,0);
    if(a[d]>=k) return  true;
    for(ll i=0;i<n;i++){
        if(i!=d){
            vector<ll> dp_sub(k,0);
            for(ll j=0;j<k-1;j++){
                if(j==0 or dp[j]!=0){
                    if(j+a[i]<k){
                        dp_sub[j+a[i]]=1;
                    }else{
                        break;
                    }
                }
            }
            for(ll j=0;j<k;j++){
                if(dp_sub[j]==1){
                    dp[j]=1;
                    if(j+a[d]>=k) return true;
                }
            }
        }
    }
    return false;
}

signed main(){
    cin >> n >> k;
    a.resize(n);
    for(ll i=0;i<n;i++){cin >> a[i];}
    sort(a.begin(),a.end());
    ll l=0;ll r=n-1;
    while(l+1<r){
        ll d=floor(l+r)/2;
        if(check(d)){
            r=d;
        }else{
            l=d;
        }
    }
    if(check(l)){
        cout << l << endl;
    }else if(check(r)){
        cout << r << endl;
    }else{
        cout << r+1 << endl;
    }
}
