#include <bits/stdc++.h>
using namespace std;
int main() {
    int t;
    cin >> t;
    while (t--) {
        int m;
        cin >> m;
        string x;
        cin >> x;
        int prev = -1;
        bool valid = true;
        for (int c : x) {
            if (c < prev) {
                cout << "NO" << endl;
                valid = false;
                break;
            }
            prev = c;
        }

        if (valid) {
            cout << "YES" << endl;
        }
    }

};