#include <bits/stdc++.h>
using namespace std;

/*
bool mystic(vector<int> a, vector<int> b) {
    for (int i = 0; i < a.size(); i++) {
        if (a[i] == b[i]) {
            return false;
        }
    }
    return true;
}


bool smaller(vector<int> a, vector<int> b) {
    for (int i = 0; i < a.size(); i++) {
        if (a[i] < b[i]) {
            return true;
        } else if (a[i] > b[i]) {
            return false;
        }
    }
    return false;
}

void permutate(vector<int> a) {
    vector<int> b = a;
    vector<int> prev;
    bool found = false;

    while (true) {
        prev_permutation(b.begin(), b.end());

        if (a == b) {
            break;
        }

        if (a[0] == b[0]) {
            continue;
        }

        if (mystic(a, b)) {
            if (!found || smaller(b, prev)) {
                prev = b;
                found = true;
            }
        } else {
            continue;
        }
    }

    for (int x : prev) {
        cout << x << " ";
    }
}
*/

int main() {
    int t, n;
    int a[1000];
    int indices[1000];
    cin >> t;
    for (int h = 0; h < t; h++) {
        cin >> n;

        for (int i = 1; i <= n; i++) {
            cin >> a[i];
            indices[i] = i;
        }

        if (n == 1) {
            cout << -1 << endl;
            continue;
        }

        for (int i = 1; i < n; i++) {
            if (a[i] == indices[i]) {
                swap(indices[i], indices[i + 1]);
            }
        }
        if (a[n] == indices[n]) {
            swap(indices[n - 1], indices[n]);
        }
        for (int i = 1; i <= n; i++)  {
            cout << indices[i] << " ";
        }
        cout << endl;
    }
}
