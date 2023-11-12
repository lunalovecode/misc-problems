#include <bits/stdc++.h>
using namespace std;

int main() {
    long long n;
    int k;
    cin >> n >> k;
    string s = to_string(n);
    for (int i = 0; i < k; i++) {
        if (n % 200 == 0) {
            n /= 200;
            s = to_string(n);
        } else {
            s += "200";
            n = stoll(s);
        }

    }
    
    cout << n << endl;
    return 0;
}