#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, l, a;
    int s = 0;
    cin >> n >> l;
    for (int i = 0; i < n; i++) {
        cin >> a;
        if (a >= l) {
            s++;
        }
    }
    cout << s << endl;
    return 0;
}