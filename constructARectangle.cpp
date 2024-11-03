#include <bits/stdc++.h>
using namespace std;

int main() {
    // if every element is unique, check if largest is equal to their sum
    // otherwise check if the sum of all three is even
    int t;
    cin >> t;
    while (t--) {
        vector<int> nums;
        for (int i = 0; i < 3; i++) {
            int x;
            cin >> x;
            nums.push_back(x);
        }

        sort(nums.begin(), nums.end());
        int sum = accumulate(nums.begin(), nums.end(), 0);

        if (nums[0] != nums[1] && nums[1] != nums[2]) {
            if (nums[0] + nums[1] == nums[2]) {
                cout << "YES" << endl;
            } else {
                cout << "NO" << endl;
            }
        } else {
            if (sum % 2 == 0) {
                cout << "YES" << endl;
            } else {
                cout << "NO" << endl;
            }
        }
    }
}