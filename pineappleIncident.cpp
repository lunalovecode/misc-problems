#include <bits/stdc++.h>
using namespace std;

bool multiple(int t, int s, int x) {
    int e = (x - t) % s;
    return e == 0;
}

/*
void intervals(int t, int s, int n) {
    vector<int> seq = {t};
    int ct = 1;
    for (int i = 1; i < n; i++) {
        if (i % 2 == 1) {
            seq.push_back(t + (ct * s));
            ct++;
        } else {
            seq.push_back(seq[i - 1] + 1);
        }
    }
    for (auto s : seq) {
        cout << s << endl;
    }
}
*/

int main() {
    int t, s, x;
    cin >> t >> s >> x;
    // intervals(t, s, 14);
    bool ans = multiple(t, s, x) || multiple(t + 1, s, x);
    if (x < t) {
        ans = false;
    }
    if (x == t + 1) {
        ans = false;
    }

    cout << (ans ? "YES" : "NO") << endl;
}