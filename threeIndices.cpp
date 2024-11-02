#include <bits/stdc++.h>
using namespace std;

int main() {
    int t, n;
    cin >> t;
    for (int h = 0; h < t; h++) {
        cin >> n;
        vector<int> a;
        bool found = false;
        for (int i = 0; i < n; i++) {
            int x;
            cin >> x;
            a.push_back(x);
        }

        for (int j = 1; j < n - 1; j++) {
            if (a[j - 1] < a[j] && a[j] > a[j + 1]) {
                found = true;
                cout << "YES" << endl;
                cout << j << " " << j + 1 << " " << j + 2 << endl;
                break;
            }
        }

        if (!found) {
            cout << "NO" << endl;
        }
    }
}