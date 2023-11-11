#include <bits/stdc++.h>
using namespace std;

void solve(int size, vector<string> solved) {
    map<char, int> numsSolved;
    numsSolved['A'] = 0;
    numsSolved['B'] = 0;
    numsSolved['K'] = 0;
    numsSolved['D'] = 0;
    for (int i = 0; i < size; i++) {
        string contestant = solved[i];
        int n = solved[i].size();
        for (int j = 0; j < n; j++) {
            numsSolved[contestant[j]]++;
        }
    }
    
    for (auto& s : {'A', 'B', 'K', 'D'}) {
        cout << numsSolved[s] << " ";
    }
}

int main() {
    int n;
    string problem;
    cin >> n;
    vector<string> solved;
    for (int i = 0; i < n; i++) {
        cin >> problem;
        solved.push_back(problem);
    }
    solve(n, solved);
    return 0;
}