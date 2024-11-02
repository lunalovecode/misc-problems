#include <bits/stdc++.h>
using namespace std;

pair<int, int> subtract(pair<int, int>time, int mins) {
    int h = time.first;
    int m = time.second - mins;
    if (m < 0) {
        h--;
        m = 60 + (time.second - mins);
    }
    return make_pair(h, m);
}

int main() {
    int x, h, m;
    cin >> x;
    cin >> h >> m;
    bool found = false;
    pair<int, int> time = {h, m};
    int pressed = 0;
    while (!found) {
        string hh = to_string(time.first);
        string mm = to_string(time.second);
        if (hh.find("7") != string::npos || mm.find("7") != string::npos) {
            found = true;
        } else {
            time = subtract(time, x);
            pressed++;
        }
    }
    cout << pressed << endl;
}