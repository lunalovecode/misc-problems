#include <bits/stdc++.h>
using namespace std;

long double distance(pair<int, int> point1, pair<int, int> point2) {
    long double x1 = point1.first;
    long double x2 = point2.first;
    long double y1 = point1.second;
    long double y2 = point2.second;
    long double ans = sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2));
    return ans;
}

int main() {
    // find distance between each point and the next
    // multiply that by k and divide by 50
    int n;
    double k;
    cin >> n >> k;
    vector<pair<int, int>> coords;
    for (int i = 0; i < n; i++) {
        pair<int, int> temp;
        cin >> temp.first >> temp.second;
        coords.push_back(temp);
    }

    long double time = 0.0;
    for (int i = 0; i < n - 1; i++) {
        long double d = distance(coords[i], coords[i + 1]);
        time += d;
    }

    time *= (double)k;
    time /= 50.0;
    cout << setprecision(30) << time << endl;
}
