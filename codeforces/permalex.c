#include <stdio.h>
#include <string.h>

int sort_str(char s[31]){
    int s_len = strlen(s);
    char tmp;
    int changes = 0;

    for (int i = 0; i < s_len; i++){
        for (int j = i + 1; j < s_len; j++){
            if (s[i] > s[j]){
                tmp = s[i];
                s[i] = s[j];
                s[j] = tmp;
                changes++;
            }
        }
    }

    return changes;
}

int sort_str_inv(char s[31]){
    int s_len = strlen(s);
    char tmp;
    int changes = 0;

    for (int i = 0; i < s_len; i++){
        for (int j = i + 1; j < s_len; j++){
            if (s[i] < s[j]){
                tmp = s[i];
                s[i] = s[j];
                s[j] = tmp;
                changes++;
            }
        }
    }

    return changes;
}

int run_perm(char s_src[31], char s_target[31], int changes, int idx){
    if (strcmp(s_src, s_target)) return changes;

    int tmp = s_src[0];
    for (int i = idx; s_src[i] != '\n'; i++){
        if (tmp < s_src[i]){
            s_src[i - 1] = s_src[i];
            s_src[i] = tmp;
            changes = run_perm(s_src, s_target, ++changes, ++idx);
        }
        tmp = s_src[i];
    }

    return changes;
}

int calc_fat(int n){
    int count = 1;
    while (n){
        count *= n--;
    }
}

void calc_occurrences(char s[31], int hash[27], int len){
    int repeats = 0;

    while (len--) hash[s[len] - 97] += 1;
}

int total_perm(char s[31]){
    int s_len = strlen(s);
    int hash[27] = {0};
    int sum = 1;


    int n_fat = calc_fat(s_len);
    calc_occurrences(s, hash, s_len);

    for (int i = 0; i < 27; i++){
        if (hash[i] == 0) continue;
        sum *= calc_fat(hash[i]);
    }

    return n_fat / sum;
}

int main(){

    char s[31], s_origin[31];

    while (scanf(" %s", s)){
        if (s[0] == '#') return 0;
        strcpy(s_origin, s);
        int changes = sort_str(s);
        int perm = total_perm(s);
        printf("%2d: %10s | %10s | %5d\n", changes, s, s_origin, perm);

        int perms = run_perm(s, s_origin, 0, 0);
        printf("%3d\n\n", perms + 1);
    }

    return 0;
}