#include <bits/stdc++.h>
using namespace std;

bool is326Num(int num) {
    vector<int> digits;
    while (num != 0) {
        digits.push_back(num % 10);
        num /= 10;
    }

    if (digits[2] * digits[1] == digits[0]) {
        return true;
    } else {
        return false;
    }
    
}

int main() {
    int n;
    scanf("%d", &n);
    
    while (!is326Num(n)) {
        n += 1;
    }
    
    printf("%d", n);
    return 0;
}