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
    
    int q, i;
    scanf("%d", &q);
    for (int j = 0; j < q; j++) {
        scanf("%d", &i);
        if (i - 1 < 0 || i - 1 >= n) {
            printf("INVALID\n");
        } else {
            printf("%d\n", a[i - 1]);
        }
    }
}