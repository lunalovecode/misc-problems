#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <string.h>
#include <cstring>
using namespace std;
long long mod = 1000000007;
long long power(int a, int b) {
    if (b == 0) {
        return 1;
    } else if (b % 2 == 0) {
        long long c = power(a, b / 2);
        return c * c % mod;
    } else {
        long long c = power(a, b / 2);
        return c * c * a % mod;
    }
}

int main() {
    int n, a, b;
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d %d", &a, &b);
    }

    printf("%ll", power(a, b));

    return 0;
}