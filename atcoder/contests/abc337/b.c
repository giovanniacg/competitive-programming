#include <stdio.h>

void complete_game(char game[8][8], int i, int j){
    for (int m = 0; m < 8; m++){
        if (m == i)
            for (int n = 0; n < 8; n++){
                if (game[m][n] == '.')
                    game[m][n] = '-';
            }
        else
            if (game[m][j] == '.')
                game[m][j] = '-';
    }
}

void debug_game(char game[8][8]){
    for (int i = 0; i < 8; i++){
        for (int j = 0; j < 8; j++)
            printf("%c", game[i][j]);
        printf("\n");
    }
}

int main(){
    char game[8][8];
    int count = 0;

    for (int i = 0; i < 8; i++)
        for (int j = 0; j < 8; j++)
            scanf(" %c", &game[i][j]);
    
    for (int i = 0; i < 8; i++)
        for (int j = 0; j < 8; j++)
            if (game[i][j] == '#'){
                // printf("i: %d, j: %d\n", i, j);
                // debug_game(game);
                complete_game(game, i, j);
                // printf("after\n");
                // debug_game(game);
            }

    for (int i = 0; i < 8; i++)
        for (int j = 0; j < 8; j++)
            if (game[i][j] == '.') count++;

    printf("%d\n", count);

    return 0;
}