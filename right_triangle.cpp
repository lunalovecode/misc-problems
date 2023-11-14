#include <bits/stdc++.h>
using namespace std;

int solve(int a, int b) {
    return (a * b) / 2;
};

int main() {
    int a, b, c;
    cin >> a >> b >> c;
    cout << solve(a, b) << endl;
    return 0;
};