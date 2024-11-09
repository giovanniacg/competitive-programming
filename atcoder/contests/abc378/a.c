#include <stdio.h>

int main(){
    int numbers[4] = {0, 0, 0, 0};
    int hash[4] = {0, 0, 0, 0};
    int count = 0;

    scanf(" %d %d %d %d", &numbers[0], &numbers[1], &numbers[2], &numbers[3]);

    for (int i = 0; i < 4; i++){
        hash[numbers[i] - 1] += 1;
    }

    for (int i = 0; i < 4; i++){
        if (hash[i] > 1 && hash[i] != 4) count++;
        if (hash[i] == 4) count = 2;
    }

    printf("%d\n", count);
}