#include <bits/stdc++.h>
using namespace std;

int main() {
    int t;
    int n;
    cin >> t;
    int greatest = -1000000;
    for (int i = 0; i < t; i++) {
        cin >> n;
        double s = sqrt(n);
        double t = floor(s);
        if (t * t != n) {
            greatest = max(greatest, n);
        }
    }
    cout << greatest << endl;
}