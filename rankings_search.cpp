#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    string contestantName;
    int score;
    cin >> n;
    map<string, int> allContestants;
    for (int i = 0; i < n; i++) {
        cin >> contestantName >> score;
        allContestants[contestantName] = i + 1;
    }
    
    int s;
    cin >> s;
    string query;
    for (int j = 0; j < s; j++) {
        cin >> query;
        cout << allContestants[query] << endl;
    }
    return 0;
}