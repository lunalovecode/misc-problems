#include <bits/stdc++.h>
using namespace std;

int main() {
    int t, a, b;
    cin >> t;
    for (int h = 0; h < t; h++) {
        cin >> a >> b;
        /*
        (c - a) + (b - c) = 
        c - a + b - c =
        c - c - a + b =
        -a + b =
        b - a
        */
       cout << (b - a) << endl;
    }
}