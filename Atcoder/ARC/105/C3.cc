#pragma GCC optimize("Ofast")

#include<bits/stdc++.h>
using namespace std;

#define REP(i,n) for(int i=0;i<int(n);i++)
#define REPD(i,n) for(int i=n-1;i>=0;i--)
#define SIZE(x) int(x.size())
#define INF 2000000000
#define PB push_back
#define F first 
#define S second

int w[8];
pair<int,int> partsx[100000];
bool info[100000];
int n,m;
vector<pair<int,int>> parts;

inline int read(){
	int x=0,w=0;char ch=0;
	while(!isdigit(ch)){w|=ch=='-';ch=getchar();}
	while(isdigit(ch)){x=(x<<1)+(x<<3)+(ch^48);ch=getchar();}
	return w?-x:x;
}

signed main(){
    n=read();m=read();
    REP(i,n)w[i]=read();
    sort(w,w+n);
    REP(i,m){partsx[i].F=read();partsx[i].S=read();}
    sort(partsx,partsx+m);
    int ma=INF;
    REP(i,m)ma=min(ma,partsx[i].S);
    if(ma<w[n-1]){
        cout<<-1<<endl;
        return 0;
    }
    REP(i,m)info[i]=true;
    REPD(i,m){
        if(!info[i])continue;
        REP(j,i){
            if(partsx[i].S<=partsx[j].S){
                info[j]=false;
            }
        }
    }
    REP(i,m)if(info[i])parts.PB(partsx[i]);
    m=SIZE(parts);
    int ans=INF;
    vector<int> dp(n,0);
    do{
        dp.assign(n,0);
        REP(j,n-1){
            int k=j;int check=w[k];
            REP(i,m){
                while(k!=n){
                    if(parts[i].S<check){
                        dp[k]=max(dp[j]+parts[i].F,dp[k]);
                        break;
                    }
                    k++;
                    check+=w[k];
                }
                if(k==n){
                    dp[n-1]=max(dp[j],dp[n-1]);
                    break;
                }
            }
        }
        ans=min(ans,dp[n-1]);
    }while(next_permutation(w,w+n-1));
    cout<<ans<<endl;
}