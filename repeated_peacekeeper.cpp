#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <string.h>
#include <cstring>
using namespace std;

int main() {
    int t, n;
    scanf("%d", &t);
    
    for (int i = 0; i < t; i++) {
        scanf("%d", &n);
        if (n % 2 == 0) {
            printf("EVENING SAVED\n");
        } else {
            printf("EVENING RUINED\n");
        }
    }
}