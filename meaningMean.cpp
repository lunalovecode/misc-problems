#include <bits/stdc++.h>
using namespace std;

void reduce(priority_queue<long long, vector<long long>, greater<long long>> a) {
    int i = 0;
    int j = 1;
    while (a.size() > 1) {
        long long x = a.top();
        a.pop();
        long long y = a.top();
        a.pop();
        long long z = floor((x + y) / 2.0);
        a.push(z);
    }
    cout << a.top() << endl;
}

int main() {
    int t, n;
    cin >> t;
    for (int h = 0; h < t; h++) {
        cin >> n;
        long long x;
        priority_queue<long long, vector<long long>, greater<long long>> a;
        for (int i = 0; i < n; i++) {
            cin >> x;
            a.push(x);
        }
        reduce(a);
    }
}