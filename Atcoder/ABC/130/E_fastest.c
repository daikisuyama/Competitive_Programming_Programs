#pragma GCC optimize("O3")

#include<stdio.h>

typedef unsigned int ll;

#define REP(i,n) for(ll i=0;i<n;i++)
#define MOD 1000000007 //10^9+7:合同式の法

ll s[2001],t[2001],dp[2001][2001],n,m={0};

signed main(){
    //入力の高速化用のコード
    scanf("%d %d",&n,&m);
    REP(i,n)scanf("%d",s+i);
    REP(i,m)scanf("%d",t+i);
    REP(i,n+1){dp[i][0]=1;}
    REP(i,m+1){dp[0][i]=1;}
    REP(i,n){
        REP(j,m){
            if(s[i]==t[j]){
                dp[i+1][j+1]+=(dp[i+1][j]+dp[i][j+1])%MOD;
            }else{
                dp[i+1][j+1]+=(dp[i+1][j]+dp[i][j+1]-dp[i][j]+MOD)%MOD;
            }
        }
    }
    printf("%d\n",dp[n][m]);
}