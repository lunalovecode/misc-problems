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
    
    vector<string> suspects;
    
    char name[100];
    for (int i = 0; i < n; i++) {
        scanf("%s", name);
        int name_len = strlen(name);
        if (name_len == 6) {
            name[6] = '\0';
            suspects.push_back(name);
        }
    }
    
    sort(suspects.begin(), suspects.end());

    int hitlist_len = suspects.size();
    if (hitlist_len < 1) {
        printf("NO SUSPECTS");
    } else {
        for (int j = 0; j < hitlist_len; j++) {
            printf("%s ", suspects[j].c_str());
        }
    }
    return 0;
}