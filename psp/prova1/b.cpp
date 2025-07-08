#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, M;
    cin >> N >> M;

    vector<int> E(N), B(M);
    for (int i = 0; i < N; i++) {
        cin >> E[i];
    }
    for (int j = 0; j < M; j++) {
        cin >> B[j];
    }

    sort(E.rbegin(), E.rend());
    sort(B.rbegin(), B.rend());

    int i = 0, j = 0, count = 0;
    while (i < N && j < M) {
        if (E[i] >= B[j]) {
            count++;
            i++;
        }
        j++;
    }

    cout << count << "\n";
    return 0;
}
