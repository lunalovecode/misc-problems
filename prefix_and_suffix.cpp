#include <bits/stdc++.h>
using namespace std;

int solve(string& s, string& t, int sLength, int tLength) {
    bool prefix = true;
    bool suffix = true;
    for (int i = 0; i < sLength; i++) {
        if (s[i] != t[i]) {
            prefix = false;
            break;
        }
    }

    for (int j = 0; j < sLength; j++) {
        if (s[j] != t[tLength - sLength + j]) {
            suffix = false;
            break;
        }
    }
    
    if (prefix == true && suffix == true) {
        return 0;
    } else if (prefix == true) {
        return 1;
    } else if (suffix == true) {
        return 2;
    } else {
        return 3;
    }
    
}

int main() {
    int n, m;
    string s, t;
    cin >> n >> m;
    cin >> s;
    cin >> t;
    cout << solve(s, t, n, m) << endl;
    return 0;
}