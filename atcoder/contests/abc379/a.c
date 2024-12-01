#include <stdio.h>

int main(){

    int n[3], i = 0;

    while (scanf(" %c", &n[i]) == 1 && ++i);

    printf("%c%c%c %c%c%c\n", n[1], n[2], n[0], n[2], n[0], n[1]);

    return 0;
}