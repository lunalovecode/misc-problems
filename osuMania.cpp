#include <bits/stdc++.h>
using namespace std;
int main() {
    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        vector<int> order;
        for (int i = 0; i < n; i++) {
            string row;
            cin >> row;
            for (int j = 0; j < 4; j++) {
                int c = row[j];
                if (c == 35) { // ascii values yippee
                    order.push_back(j + 1);
                }
            }
        }
        for (int i = order.size() - 1; i >= 0; i--) {
            cout << order[i] << " ";
        }
        cout << endl;
    }
};