#include <bits/stdc++.h>
using namespace std;
int main() {
    int n, k;
    cin >> n >> k;
    vector<int> coords;
    for (int i = 0; i < n; i++) {
        int x;
        cin >> x;
        coords.push_back(x);
    }
    sort(coords.begin(), coords.end(), greater<int>());

    bool found = false;
    int xy = 0;
    if (k > n) {
        cout << -1 << endl;
    } else {
        cout << coords[k - 1] << " " << coords[k - 1] << endl;
    }
};