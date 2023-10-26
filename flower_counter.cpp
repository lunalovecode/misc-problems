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
    
    for (int x = 0; x < n; x++) {
        int flower;
        scanf("%d", &flower);
        a.push_back(flower);
    }
    
    int q;
    scanf("%d", &q);
    
    for (int y = 0; y < q; y++) {
        int i, j, x;
        int ct = 0;
        scanf("%d %d %d", &i, &j, &x);
        for (int z = i - 1; z < j; z++) {
            if (a[z] <= x) {
                ct++;
            }
        }
        printf("%d \n", ct);
    }
    
    return 0;
}