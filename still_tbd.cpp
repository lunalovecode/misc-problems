#include <bits/stdc++.h>
using namespace std;

bool solve(vector<int> date) {
    if (date[1] > 4) {
        return false;
    } else if (date[1] == 4 && date[2] > 30) {
        return false;
    } else {
        return true;
    }
}

int main() {
    string s;
    cin >> s;
    vector<int> date = {stoi(s.substr(0, 3)), stoi(s.substr(5, 6)), stoi(s.substr(8, 9))};
    cout << (solve(date) ? "Heisei" : "TBD") << endl;
    return 0;
};