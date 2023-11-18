#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <set>
#include <map>
#include <algorithm>
using namespace std;


int main() {
    int n, q, y;
    string x;
    map<string, int> m;
    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> q >> x;
        map<string,int>::iterator itr=m.find(x);
        if (itr == m.end()) {
            m.insert(make_pair(x, 0));
        }

        if (q == 1) {
            cin >> y;
            m[x] += y;
        } else if (q == 2) {
            m[x] = 0;
        } else {
            cout << m[x] << endl;
        }
    }
    return 0;
}



