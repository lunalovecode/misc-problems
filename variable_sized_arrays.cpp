#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int n, q, k, c;
    scanf("%d %d", &n, &q);
    vector<vector<int>> w;
    
    for (int a = 0; a < n; a++) {
        scanf("%d", &k);
        vector<int> v;
        
        for (int b = 0; b < k; b++) {
            scanf("%d", &c);
            v.push_back(c);
        }
        
        w.push_back(v);
    }
    
    int i, j;
    for (int d = 0; d < q; d++) {
        scanf("%d %d", &i, &j);
        printf("%d\n", w[i][j]);
    }
    
    return 0;
}