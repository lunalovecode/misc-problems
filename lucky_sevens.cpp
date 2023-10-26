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
    vector<int> bananas;
    
    for (int i = 0; i < n; i++) {
        int bunch;
        scanf("%d", &bunch);
        bananas.push_back(bunch);
    }
    
    int bought = 0;
    for (int j = 0; j < n; j++) {
        if (bananas[j - 1] == 7 || bananas[j] == 7 || bananas[j + 1] == 7) {
            bought += bananas[j];
        }
    }
    
    printf("%d", bought);
}