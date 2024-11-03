#include <bits/stdc++.h>
using namespace std;

vector<vector<int>> combos;
void generateCombinations(vector<int>& nums, vector<int>& combination, int index, int n, int k) {
    if (combination.size() == k) {
        vector<int> temp;
        for (int i = 0; i < k; i++) {
            temp.push_back(combination[i]);
        }
        combos.push_back(temp);
        return;
    }

    for (int i = index; i < nums.size(); i++) {
        combination.push_back(nums[i]);
        generateCombinations(nums, combination, i + 1, n, k);
        combination.pop_back();
    }
}

int main() {
    // check if there's a combination such that a + b >= c
    vector<int> nums;
    string ans = "IMPOSSIBLE";
    for (int i = 0; i < 4; i++) {
        int x;
        cin >> x;
        nums.push_back(x);
    }

    vector<int> combination;
	generateCombinations(nums, combination, 0, 4, 3);
    for (vector<int> c : combos) {
        sort(c.begin(), c.end());
        if (c[0] + c[1] > c[2]) {
            ans = "TRIANGLE";
            break;
        } else if (c[0] + c[1] == c[2]) {
            ans = "SEGMENT";
        }
    }

    cout << ans << endl;
}