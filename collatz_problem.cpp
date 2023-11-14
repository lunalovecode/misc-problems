#include <bits/stdc++.h>
using namespace std;

int solve(int s) {
    bool go = true;
    int n = s, i = 0;
    vector<int> usedTerms = {};
    while (go) {
        if (count(usedTerms.begin(), usedTerms.end(), n)) {
            go = false;
        } else {
            usedTerms.push_back(n);
        }
        if (n % 2 == 0) {
            n /= 2;
        } else {
            n = (3 * n) + 1;
        }
        i++;
    }
    return i;
};

int main() {
    int s;
    cin >> s;
    cout << solve(s) << endl;
    return 0;
};