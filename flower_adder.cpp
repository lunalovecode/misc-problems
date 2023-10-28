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
    
    int flower;
    for (int i = 0; i < n; i++) {
        scanf("%d", &flower);
        a.push_back(flower);
    }
    
    int q, i, k;
    scanf("%d", &q);
    for (int j = 0; j < q; j++) {
        scanf("%d %d", &i, &k);
        a[i - 1] += k;
    }
    
    for (int j = 0; j < n; j++) {
        printf("%d ", a[j]);
    }
    
}