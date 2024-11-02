#include <bits/stdc++.h>
using namespace std;
int main() {
    string wall;
    cin >> wall;
    int trips = 0;
    int carrying = 0;
    char prev;
    bool first = true;
    for (char x : wall) {
        if (first) {
            prev = x;
            first = false;
            carrying++;
            continue;
        }
        
        if (prev == x) {
            if (carrying < 5) {
                carrying++;
            } else {
                carrying = 1;
                trips++;
            }
        } else {
            trips++;
            carrying = 1;
        }

        prev = x;
    }

    if (carrying > 0) {
        trips++;
    }

    cout << trips << endl;
};