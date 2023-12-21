#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, m, a, b;
    cin >> n >> m;
    vector<vector<int>> table(n, vector<int>(n, 0));
    for (int i = 0; i < m; i++) {
        cin >> a >> b;
        table[a - 1][b - 1]++;
        table[b - 1][a - 1]++;
    };

    for (int i = 0; i < n; i++) {
        cout << accumulate(table[i].begin(), table[i].end(), 0) << endl;
    }
}