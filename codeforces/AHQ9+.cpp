#include <bits/stdc++.h>
using namespace std;

// Macros úteis
#define fastio ios::sync_with_stdio(0); cin.tie(0)
#define ll long long
#define pb push_back
#define all(x) (x).begin(), (x).end()
#define endl '\n'

int main() {
    fastio; // Melhora a entrada e saída

    string str;

    cin >> str;

    for(char c : str){

        if(c == 'H' || c == 'Q' || c == '9'){
            cout << "YES" << endl;
            return 0;
        }
    }

    cout << "NO" << endl;

    return 0;
}
