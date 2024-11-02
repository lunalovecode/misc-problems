#include <iostream>
using namespace std;
long long n, a[200005], q, sum=0, nw[200005], t;
int main() {
    ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
    cin >> t;
    for (int i = 0; i < t; i++) {
        sum = 0;
        cin >> n >> q;
        for(int j = 1; j <= n; j++){
            cin >> a[j];
            sum += a[j];
            nw[j] = nw[j - 1];
            nw[j] += a[j];
        }
        for(int j = 0; j < q; j++){
            long long l,r,k;
            cin >> l >> r >> k;
            long long ans = nw[n] - (nw[r] - nw[l - 1]) + k * (r - l + 1);
            if (ans % 2 == 1){
                cout << "YES" << endl;
            } else {
                cout << "NO" << endl;
            }
        }
    }
}