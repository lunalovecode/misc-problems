#include <bits/stdc++.h>
using namespace std;

int main() {
    int t, m, n;
    string a;
    cin >> t;
    for (int h = 0; h < t; h++) {
        map<char, int> counts;
        cin >> m >> n;
        cin >> a;
        for (char c : a) {
            if (counts.find(c) == counts.end()) {
                counts[c] = 1;
            } else {
                counts[c]++;
            }
        }

        int total = 0;
        if (counts.size() < 7) {
            total += (7 - counts.size()) * n;
        }
        for (auto c : counts) {
            if (c.second < n) {
                total += n - c.second;
            }
        }

        cout << total << endl;
    }
}