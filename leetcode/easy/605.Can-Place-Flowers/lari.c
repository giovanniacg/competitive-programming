#include <stdio.h>

int canPlaceFlowers(int* flowerbed, int flowerbedSize, int n) {
    for (int i = 0; i < flowerbedSize; i++){
        if ((((i - 1) < 0) || flowerbed[i-1] == 0) && (flowerbed[i] == 0) && (((i+1)>=flowerbedSize) || flowerbed[i+1] == 0)){
            flowerbed[i] = 1;
            n--;
        } 
        
        if(!n) return 1;
    }
    return 0;
}

int main(){

    int flowerbed[7] = {1,0,0,0,1,0,0};
    int n = 2;

    printf("%d\n", canPlaceFlowers(flowerbed, 7, n));

    return 0;
}