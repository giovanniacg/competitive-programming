#include <stdio.h>

void sum_2(int n){
    n += 2;
}

int main(){
    int l[1000000];
    int x;

    for (int i = 1000000 - 1; i > -1; i--){
        sum_2(l[i]);
    }

    return 0;
}