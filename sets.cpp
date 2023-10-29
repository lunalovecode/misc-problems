#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <set>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    set<int> s;
    int q, y, x;
    scanf("%d", &q);
    for (int i = 0; i < q; i++) {
        scanf("%d %d", &y, &x);
        if (y == 1) {
            s.insert(x);
        } else if (y == 2) {
            s.erase(x);
        } else {
            set<int>::iterator ind = s.find(x);
            if (ind == s.end()) {
                printf("No\n");
            } else {
                printf("Yes\n");
            }
        }
    }
    return 0;
}



