#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <string.h>
#include <cstring>
using namespace std;

int main() {
    int n;
    scanf("%d", &n);
    vector<int> a;
    
    for (int h = 0; h < n; h++) {
        int flower;
        scanf("%d", &flower);
        a.push_back(flower);
    }
    
    int q;
    scanf("%d", &q);
    
    for (int k = 0; k < q; k++) {
        int i, j;
        scanf("%d %d", &i, &j);
        int x = a[i - 1];
        int y = a[j - 1];
        a[i - 1] = y;
        a[j - 1] = x;
    }
    
    for (int l = 0; l < n; l++) {
        printf("%d ", a[l]);
    }
    
    return 0;
}