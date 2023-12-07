#include <bits/stdc++.h>
using namespace std;

void solve(int M, int D, int y, int m, int d) {
    if (d + 1 > D) {
        if (m + 1 > M) {
            y++;
            m = 1;
            d = 1;
        } else {
            m++;
            d = 1;
        }
    } else {
        d++;
    }
    cout << y << " " << m << " " << d << endl;
}

int main() {
    int M, D, y, m, d;
    cin >> M >> D;
    cin >> y >> m >> d;
    solve(M, D, y, m, d);
    return 0;
};