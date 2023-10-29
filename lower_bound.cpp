#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int n, q, y, z;
    vector<int> x;
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &z);
        x.push_back(z);
    }
    
    vector<int>::iterator ind;
    scanf("%d", &q);
    for (int i = 0; i < q; i++) {
        scanf("%d", &y);
        ind = lower_bound(x.begin(), x.end(), y);
        if (x[ind - x.begin()] == y) {
            printf("Yes %d\n", ind - x.begin() + 1);
        } else {
            printf("No %d\n", ind - x.begin() + 1);
        }
    }
    
    return 0;
}
