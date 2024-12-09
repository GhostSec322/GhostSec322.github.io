#include<stdio.h>
int check(int x){
    int count =0;
    for( int i=1;i<=x;i++){
        if(x%i==0){
            count++;
        }
    }
    if (count==2){
        printf("소수");
    }
    else{
        printf("소수아님");
    }
}
int main(void){
    check(11);
    return 0;
}