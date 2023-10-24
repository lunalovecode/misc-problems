#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int n;
    scanf("%d", &n);
    vector<int>v;
    int el;
    for (int i = 0; i < n; i++) {
        scanf("%d", &el);
        v.push_back(el);
    }
    sort(v.begin(), v.end());
    for (int j = 0; j < n; j++) {
        printf("%d ", v[j]);
    }
    return 0;
}
