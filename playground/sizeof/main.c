#include <stdio.h>

int main(){
    int x = 0;
    int y[4];
    y[0] = 1;
    y[1] = 2;
    y[2] = 3;
    printf("%ld\n", sizeof(y[0]));

    return 0;
}