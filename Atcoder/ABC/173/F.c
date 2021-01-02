#pragma GCC optimize("Ofast")
#include<stdio.h>

inline void swap(int* l,int* r){
    int temp=*l;
    *l=*r;
    *r=temp;
    return;
}

int main(){
    long long n,l,r,ans,i;scanf("%d",&n);
    ans=n*(n+1)*(n+2)/6;
    for(int i=0;i<n-1;i++){
        scanf("%d%d",&l,&r);
        if(l>r)swap(&l,&r);
        ans-=(l*(n-r+1));
    }
    printf("%lld",ans);
    return 0;
}