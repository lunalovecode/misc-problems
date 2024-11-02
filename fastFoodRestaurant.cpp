#include <bits/stdc++.h>
using namespace std;


int main() {
    int t;
    cin >> t;
    for (int i = 0; i < t; i++) {
        int a, b, c;
        int x, y, z;
        cin >> a >> b >> c;
        if (a < b) {
            swap(a, b);
        }
        if (a < c) {
            swap(a, c);
        }
        if (b < c) {
            swap(b, c);
        }

        int ans = 0;
        if (c) {
            ans++;
            c--;
        }
        if (b) {
            ans++;
            b--;
        }
        if (a) {
            ans++;
            a--;
        }

        if (a && b) {
            ans++;
            a--;
            b--;
        }
        if (a && c) {
            ans++;
            a--;
            c--;
        }
        if (b && c) {
            ans++;
            b--;
            c--;
        }
        if (a && b && c) {
            ans++;
            a--;
            b--;
            c--;
        }
        cout << ans << endl;
    }
}