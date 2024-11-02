#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int t;
    cin >> t;
    for (int h = 0; h < t; h++) {
        int n;
        cin >> n;
        // pair elements and sort the pairs
        vector<int> a;
        vector<int> b;
        vector<pair<int, int>> c;
        for (int i = 0; i < n; i++) {
            int x;
            cin >> x;
            a.push_back(x);
        }

        for (int i = 0; i < n; i++) {
            int x;
            cin >> x;
            b.push_back(x);
        }

        for (int i = 0; i < n; i++) {
            pair<int, int> temp(a[i], b[i]);
            c.push_back(temp);
        }

        sort(c.begin(), c.end());

        for (pair<int, int> p : c) {
            cout << p.first << " ";
        }
        cout << endl;

        for (pair<int, int> p : c) {
            cout << p.second << " ";
        }
        cout << endl;
    }
}