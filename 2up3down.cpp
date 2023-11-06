#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <string.h>
#include <cstring>
using namespace std;

int main() {
    int x, y;
    scanf("%d %d", &x, &y);
    if (x - y >= -2 && x - y <= 3) {
        printf("Yes");
    } else {
        printf("No");
    }
    return 0;
}