#include <bits/stdc++.h>
using namespace std;
 
const long long MOD = 1000000007;
 
// Fast modular exponentiation.
long long modexp(long long base, long long exp) {
    long long result = 1;
    while(exp){
        if(exp & 1) result = (result * base) % MOD;
        base = (base * base) % MOD;
        exp >>= 1;
    }
    return result;
}
 
int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
 
    string a, b;
    cin >> a >> b;
    int n = a.size();
    
    // Precompute factorials and inverse factorials up to n.
    vector<long long> fact(n+1), invfact(n+1);
    fact[0] = 1;
    for (int i=1; i<=n; i++){
        fact[i] = fact[i-1] * i % MOD;
    }
    invfact[n] = modexp(fact[n], MOD-2);
    for (int i = n; i >= 1; i--){
        invfact[i-1] = invfact[i] * i % MOD;
    }
 
    // count_less(x, freq): conta quantas permutações (do multiconjunto dado por freq) são < x.
    auto count_less = [&](const string &x, vector<int> freq) -> long long {
        long long res = 0;
        int rem = n;
        // cur_R = ∏_{l=0}^{25} invfact[freq[l]]
        long long cur_R = 1;
        for (int l = 0; l < 26; l++){
            cur_R = (cur_R * invfact[freq[l]]) % MOD;
        }
 
        for (int i = 0; i < n; i++){
            int cur = x[i] - 'a';
            int rem_minus = rem - 1;
            // Para cada letra menor que x[i] que esteja disponível...
            for (int l = 0; l < cur; l++){
                if(freq[l] > 0){
                    // Ao usar uma ocorrência da letra l, a nova contribuição do produto é:
                    // delta = invfact[freq[l]-1] * fact[freq[l]] mod MOD.
                    long long delta = (invfact[freq[l]-1] * fact[freq[l]]) % MOD;
                    res = (res + fact[rem_minus] * cur_R % MOD * delta) % MOD;
                }
            }
            if(freq[cur] == 0) break;
            int old_val = freq[cur];
            freq[cur]--;
            // Atualiza cur_R para refletir que usamos uma ocorrência de cur.
            cur_R = cur_R * (invfact[old_val-1] * fact[old_val] % MOD) % MOD;
            rem--;
        }
        return res;
    };
 
    vector<int> freq(26, 0);
    for (char c : a)
        freq[c - 'a']++;
 
    long long Fa = count_less(a, freq);
    long long Fb = count_less(b, freq);
    // Como a própria string a está no conjunto, seu “rank” (0-indexado) é Fa.
    // Queremos contar c tais que a < c < b, isto é, (Fb - Fa - 1).
    long long ans = (Fb - Fa - 1) % MOD;
    if(ans < 0) ans += MOD;
    cout << ans << "\n";
    return 0;
}
