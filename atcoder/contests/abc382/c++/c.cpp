# include <bits/stdc++.h>
using namespace std;

#define endl '\n'
#define pb push_back

int main(){
    
    list<int> client;
    map<int, int> sushi;
    list<int> chosen;
    int N, M, S, C, i = 1;

    cin >> N;
    cin >> M;

    for(int i = 0; i < N; i++){
        cin >> C;
        client.pb(C);
    }
    
    for(int i = 0; i < M; i++){
        cin >> S;
        sushi.emplace(S, i+1);
    }
    
    for(int c : client){

        for(const auto pair : sushi){
            if(c <= pair.first){
                chosen.pb(pair.second)
                cout << pair.first << " " << pair.second << endl;
                sushi.erase(pair.second);
            }
        }

        i++;

    }

    cout << endl;
    cout << endl;

    if(sushi.size() != 0) 
        for(const auto pair : sushi)
        {
            cout << pair.first << " " << pair.second << endl;
            chosen.pb(-1);
            sushi.erase(pair.second);
        }
            
    cout << "chosen" << endl;
    for(const auto pos : chosen)
        cout << pos << " ";

    cout << endl;
    return 0;
}