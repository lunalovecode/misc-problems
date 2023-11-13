#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, d, ct, s;
    cin >> n >> d;
    for (int i = 0; i < n; i++) {
        cin >> s;
        if (s <= d) {
            ct += s;
        }
    }
    
    cout << ct << endl;
};