#include <bits/stdc++.h>
using namespace std;

int solve(int a, int b) {
    if (abs(a - b) <= 1) {
        return 0;
    } else {
        return 1;
    }
}

int main() {
    int a, b;
    cin >> a >> b;
    cout << ((solve(a, b) == 0) ? "Yay!" : ":(") << endl;
    return 0;
}