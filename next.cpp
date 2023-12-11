#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, x;
    vector<int> a;
    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> x;
        a.push_back(x);
    }
    
    int max = *max_element(a.begin(), a.end());
    vector<int> b;
    
    for (int i = 0; i < n; i++) {
        if (a[i] < max) {
            b.push_back(a[i]);
        }
    }
    
    cout << *max_element(b.begin(), b.end()) << endl;
    
    return 0;
}
