#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

struct DisjointSets {
    vector<int> parent, size;
    
    DisjointSets(int n): parent(n + 1, -1), size(n + 1, 1) {};
    
    int find(int i) {
        return (parent[i] == -1) ? i : parent[i] = find(parent[i]);
    }
    
    void onion(int i, int j) {
        if ((i = find(i)) == (j = find(j))) return;
        if (size[i] > size[j]) swap(i, j);
        size[j] += size[i];
        parent[i] = j;
    }
    
    int s(int i) {
        return size[find(i)];
    }
};

int main() {
    int n, q, i, j;
    char type;
    cin >> n >> q;
    DisjointSets d(n);
    for (int ct = 0; ct < q; ct++) {
        cin >> type >> i;
        if (type == 'M') {
            cin >> j;
            d.onion(i, j);
        } else {
            cout << d.s(i) << endl;
        }
    }
    return 0;
}
