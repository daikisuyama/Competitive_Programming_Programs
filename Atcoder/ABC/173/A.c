#include<stdio.h>
int main(){
    int n;
    scanf("%d",&n);
    while(n>1000)n-=1000;
    printf("%d",1000-n);
}