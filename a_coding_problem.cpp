// beep beep
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int n;
    scanf("%d", &n);
    
    vector<int> odds;
    vector<int> evens;
    
    for (int i = 0; i < n; i++) {
        int plate_num;
        scanf("%d", &plate_num);
        if (plate_num % 2 == 0) {
            evens.push_back(plate_num);
        } else {
            odds.push_back(plate_num);
        }
    }
    
    sort(odds.begin(), odds.end());
    sort(evens.begin(), evens.end());
    
    int odd_len = odds.size();
    int even_len = evens.size();
    
    for (int o = 0; o < odd_len; o++) {
        printf("%d ", odds[o]);
    }
    
    printf("\n");
    
    for (int e = 0; e < even_len; e++) {
        printf("%d ", evens[e]);
    }
    
}