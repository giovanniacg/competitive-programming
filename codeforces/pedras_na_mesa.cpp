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
    int size;

    cin >> size;
    cin >> str;

    int count = 0;

    for(int i = 0; i < size-1; i++)
        if(str[i] == str[i+1]) count++;
            
    cout << count << endl;

    return 0;
}
