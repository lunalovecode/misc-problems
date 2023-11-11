#include <bits/stdc++.h>
using namespace std;

bool compare(const pair<string, int>& a, const pair<string, int>& b) {
    if (a.second != b.second) {
        return a.second > b.second;
    }
    
    return a.first < b.first;
}

void solve(vector<pair<string, int>> solved) {
    sort(solved.begin(), solved.end(), compare);
    map<string, int>::iterator i;
    for_each(solved.begin(), solved.end(), [](pair<string, int> p) {
        cout << p.first << " " << p.second << endl;
    });
}

int main() {
    int n;
    string contestantName;
    int score;
    cin >> n;
    vector<pair<string, int>> allContestants;
    for (int i = 0; i < n; i++) {
        cin >> contestantName >> score;
        allContestants.push_back(pair<string, int>(contestantName, score));
    }
    
    solve(allContestants);
    return 0;
}