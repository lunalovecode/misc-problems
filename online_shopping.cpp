#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, s, k, p, q;
    int cost = 0;
    cin >> n >> s >> k;
    for (int i = 0; i < n; i++) {
        cin >> p >> q;
        cost += (p * q);
    }
    
    if (cost < s) {
        cout << cost + k << endl;
    } else {
        cout << cost << endl;
    }
    
}