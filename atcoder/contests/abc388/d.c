#include <stdio.h>

int main(){

    int N, i, aliens[100005];

    scanf(" %d", &N);

    for (i = 0; i < N; i++){
        scanf(" %d", &aliens[i]);
    }

    for (i = 0; i < N; i++){
        for (int k = 0; k < i; k++){
            if (aliens[k] > 0){
                aliens[k]--;
                aliens[i]++;
            }
        }
    }

    printf("%d", aliens[0]);
    for (i = 1; i < N; i++){
        printf(" %d", aliens[i]);
    }
    printf("\n");
    return 0;
}