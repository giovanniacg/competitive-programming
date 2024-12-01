# include <bits/stdc++.h>
using namespace std;

#define endl '\n'

int main(){
    int N, D, i = 0;
    string cookies;

    cin >> N >> D;
    cin >> cookies;

    for(char c : cookies){
        if(c == '@') i++;
    }
    cout << (N-i+D) << endl;
    return 0;
}