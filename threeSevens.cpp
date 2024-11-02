#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        
        map<int,int> last;
        
        for (int j = 1; j <= n; j++){
            int p;
            cin >> p;
            for(int k = 1; k <= p; k++){
                int x;
                cin >> x;
                last[x] = j;
            }
        }
        
        vector<int> ans(n, -1);
        set<int> unique;
        for(auto [f, s] : last){
            if(ans[s - 1] == -1){
                ans[s - 1] = f;
                unique.insert(f);
            }
        }
        if (unique.size() != n) {
            cout << -1 << endl;
        }
        else {
            for (int a : ans) {
                cout << a << " ";
            }
            cout << "\n";
        }
    }
}