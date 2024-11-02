#include <bits/stdc++.h>
using namespace std;

// i am ashamed of my solution for the overflow, but at least it works
// https://codeforces.com/group/nAxxdTBTfr/contest/557812/submission/286654387
long long int n;
vector<long long int> a;
vector<long long int> b;

long long int block_start(long long int j) {
	double s = ceil(sqrt(n));
	return s * j;
}

long long int block_end(long long int j) {
	double s = ceil(sqrt(n));
	long long int i = (s - 1) + (s * j);
	return min(i, n - 1);
}

long long int block_containing(long long int i) {
    double s = ceil(sqrt(n));
    return ceil((i - s + 1) / s);
}

long long int compute(long long int j) {
    long long int n = a.size();
    long long int total = 0;
    for (long long int i = block_start(j); i <= block_end(j); i++) {
        total += a[i];
    }
    return total;
}

void set_value(long long int i, long long int k) {
	long long int block = block_containing(i);
	b[block] -= a[i];
	a[i] = k;
	b[block] += k;
}

long long int sum_values(long long int l, long long int r) {
	long long int sum = 0;
	long long int lBlock = block_containing(l);
	long long int rBlock = block_containing(r);
	long long int startBlock = -1, endBlock = -1;
	long long int startExcess1 = -1,endExcess1 = -1;
	long long int startExcess2 = -1, endExcess2 = -1;

	if (lBlock == rBlock || lBlock + 1 == rBlock) {
		startExcess1 = l;
		endExcess1 = r;
	} else {
		startBlock = lBlock + 1;
		endBlock = rBlock - 1;
		startExcess1 = l;
		endExcess1 = block_end(lBlock);
		startExcess2 = block_start(rBlock);
		endExcess2 = r;
	}

	if (startBlock > -1 && endBlock > -1) {
		for (long long int i = startBlock; i <= endBlock; i++) {
			sum += b[i];
		}
	}

	if (startExcess1 > -1 && endExcess1 > -1) {
		for (long long int i = startExcess1; i <= endExcess1; i++) {
			sum += a[i];
		}
	}

	if (startExcess2 > -1 && endExcess2 > -1) {
		for (long long int i = startExcess2; i <= endExcess2; i++) {
			sum += a[i];
		}
	}

	return sum;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cin >> n;

    /*
	task 1
    int f;
    cin >> f;
    string op;
    int k;
    for (int i = 0; i < f; i++) {
        cin >> op >> k;
        if (op == "s") {
            cout << block_start(n, k) << endl;
        } else if (op == "e") {
            cout << block_end(n, k) << endl;
        } else {
            cout << block_containing(n, k) << endl;
        }
    }
    */

    string op;
    for (int i = 0; i < n; i++) {
        long long int x;
        cin >> x;
        a.push_back(x);
    }
    long long int m;
    cin >> m;

    double s = ceil(sqrt(n));
    long long int x = ceil(n / s);

    for (long long int i = 0; i < x; i++) {
        b.push_back(compute(i));
    }

    long long int l, r;
    for (long long int i = 0; i < m; i++) {
        cin >> op >> l >> r;
        if (op == "SUM") {
            cout << sum_values(l, r) << endl;

        } else {
            set_value(l, r);
        }
    }
}