#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int n;
    scanf("%d", &n);
    vector<int> v;
    for (int i = 0; i < n; i++) {
        int z;
        scanf("%d", &z);
        v.push_back(z);
    }
    
    int x;
    scanf("%d", &x);
    
    int a, b;
    for (int j = 0; j < 2; j++) {
        scanf("%d %d", &a, &b);
    }
    
    v.erase(v.begin() + x - 1);
    v.erase(v.begin() + a - 1, v.begin() + b - 1);
    
    int len = v.size();
    printf("%d\n", len);
    
    for (int k = 0; k < len; k++) {
        printf("%d ", v[k]);
    }
    return 0;
}
