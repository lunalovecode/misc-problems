#include <bits/stdc++.h>
using namespace std;
int main() {
    int t; int n;
        cin >> t;

    for (int i = 0; i < t; i++) {
        int solved = 0;
        cin >> n;
        char problems[n];
        cin >> problems;    
        vector<int> seen;
        for (int j = 0; j < n; j++) {
            if (find(seen.begin(), seen.end(), problems[j]) == seen.end()) {
                seen.push_back(problems[j]);
                solved += 2;
            } else {
                solved++;
            }
        }
        cout << solved << endl;
    };
};