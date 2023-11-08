#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, a, b;
    string ans = "Yes";
    cin >> n;
    cin >> a;
    for (int i = 0; i < n - 1; i++) {
        cin >> b;
        if (b != a) {
            ans = "No";
            break;
        }
    }
    
    cout << ans << endl;
    
    return 0;
}