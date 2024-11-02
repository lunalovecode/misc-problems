#include <bits/stdc++.h>
using namespace std;
int main() {
    int n; int m;
    cin >> n >> m;
    int columns[1000000];
    int s; int t;
    long long l[1000000];
    long long r[1000000];
    for (int h = 1; h <= n; ++h) {
        cin >> columns[h];
    }

    for (int i = 2; i <= n; ++i) {
        l[i] = l[i - 1] + max(0, columns[i - 1] - columns[i]);
    }

    for (int i = n - 1; i > 0; --i) {
        r[i] = r[i + 1] + max(0, columns[i + 1] - columns[i]);
    }


    for (int j = 0; j < m; j++) {
        cin >> s >> t;
        if (s < t) {
            cout << l[t] - l[s] << endl;
        } else {
            cout << r[t] - r[s] << endl;
        }
    }
};