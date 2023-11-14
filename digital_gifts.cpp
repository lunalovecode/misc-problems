#include <bits/stdc++.h>
using namespace std;

double convert(double amount) {
    return amount *= 380000.0;
};

int main() {
    int n;
    double x, total = 0;
    string u;
    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> x >> u;
        if (u == "BTC") {
            x = convert(x);
        }
        total += x;
    }
    cout << total << endl;
    return 0;
};