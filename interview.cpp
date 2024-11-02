#include <bits/stdc++.h>
using namespace std;

int f(int arr[], int l, int r) {
    int sum = 0;
    for (int i = l; i < r; i++) {
        sum = sum | arr[i];
    }
    return sum;
}

int main() {
    int n;
    cin >> n;
    int a[n];
    int b[n];
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }

    for (int i = 0; i < n; i++) {
        cin >> b[i];
    }

    int greatest = 0;
    int l = 0;
    int r = n;
    // do something better later
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n + 1; j++) {
            int aSum = f(a, i, j);
            int bSum = f(b, i, j);
            greatest = max(greatest, aSum + bSum);
        }
    }

    cout << greatest << endl;
}