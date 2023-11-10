#include <bits/stdc++.h>
using namespace std;

int solve(int n, string& s) {
    int ind = s.find("ABC") == s.npos ? -1 : s.find("ABC") + 1;
    return ind;
}

int main() {
    int n;
    string s;
    cin >> n;
    cin >> s;
    cout << solve(n, s) << endl;
    return 0;
}