#include<stdio.h>
#include<string.h>
int main(){
    int n,i;int d[4]={0};char s[3];
    scanf("%d\n",&n);
    for(i=0;i<n;i++){
        scanf("%s\n",s);
        if(s[0]=='A'){
            d[0]++;
        }else if(s[0]=='W'){
            d[1]++;
        }else if(s[0]=='T'){
            d[2]++;
        }else{
            d[3]++;
        }
    }
    printf("AC x %d\nWA x %d\nTLE x %d\nRE x %d\n",d[0],d[1],d[2],d[3]);
    return 0;
}