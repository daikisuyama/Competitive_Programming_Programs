#include<bits/stdc++.h>
using namespace std;
int n,m,a[100010],maxlt=-1e9,minq=1e9;
int l[100010],v[100010];
int st[100010],top=0;
int ans=2e9,dis[10],sum[10];
pair<int,int> bri[100010];
inline int read()
{
	int x=0,w=0;char ch=0;
	while(!isdigit(ch)){w|=ch=='-';ch=getchar();}
	while(isdigit(ch)){x=(x<<1)+(x<<3)+(ch^48);ch=getchar();}
	return w?-x:x;
}
int ef(int x)
{return l[lower_bound(v+1,v+1+top,x)-v-1];}
int main()
{
	n=read();m=read();
	for(int i=1;i<=n;i++)
		maxlt=max(maxlt,(a[i]=read()));
	sort(a+1,a+1+n);
	swap(a[1],a[n-1]);
	for(int i=1;i<=m;i++){
		l[i]=read(),v[i]=read();
		bri[i]={l[i],v[i]};
		minq=min(minq,v[i]);
	}
	if(minq<maxlt){printf("-1\n");return 0;}
	sort(bri+1,bri+1+m);
	top=0;
	for(int i=1;i<=m;st[++top]=i++)
		while(top>0&&bri[i].second<=bri[st[top]].second)top--;
	for(int i=1;i<=top;i++)
		l[i]=bri[st[i]].first,v[i]=bri[st[i]].second;
	do{
		for(int i=0;i<10;dis[i++]=0);
		for(int i=1;i<=n;i++){
			sum[i]=sum[i-1]+a[i];
			for(int j=1;j<i;j++)
				dis[i]=max(dis[i],dis[j]+ef(sum[i]-sum[j-1]));
		}
		ans=min(ans,dis[n]);
	}while(next_permutation(a+2,a+n));
	cout<<ans<<'\n';
}