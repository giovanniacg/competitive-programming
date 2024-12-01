# include <bits/stdc++.h>
using namespace std;

#define endl '\n'

int main(){
    int N, D, i = 0;
    string cookies;

    cin >> N >> D;
    cin >> cookies;

    for(auto c = cookies.end(); D!=0; c--){
        if(*c == '@') {
            *c = '.';
            D--;
        }
    }
    cout << cookies << endl;
    return 0;
}