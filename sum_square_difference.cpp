#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;
    int sumOfSquares = (n * (n + 1) * ((2 * n) + 1)) / 6;
    int squareOfSums = pow((n * (n + 1)) / 2, 2);
    cout << (squareOfSums - sumOfSquares) << endl;
    return 0;
}