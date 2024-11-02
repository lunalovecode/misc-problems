#include <bits/stdc++.h>
using namespace std;

// not necessary but could help with debugging
int time(string password) {
    int t = 2;
    for (int i = 1; i < password.size(); i++) {
        if (password[i] == password[i - 1]) {
            t++;
        } else {
            t += 2;
        }
    }
    return t;
}

string insrt(string password) {
    vector<char> nw;
    char chr;
    bool inserted = false;
    for (int i = 0; i < password.size(); i++) {
        nw.push_back(password[i]);
        if (password[i] == password[i + 1] && !inserted) {
            char ps = static_cast<int>(password[i]);
            if (ps < 122) {
                chr = static_cast<int>(password[i]) + 1;
            } else {
                chr = 121;
            }
            nw.push_back(chr);
            inserted = true;
        }
    }

    if (!inserted) {
        char ps = static_cast<int>(password[password.size() - 1]);
        if (ps < 122) {
            chr = ps + 1;
        } else {
            chr = 121;
        }
        nw.push_back(chr);
    }

    string nwstr;
    for (char c : nw) {
        nwstr += c;
    }

    return nwstr;
}

int main() {
    int t;
    cin >> t;
    char chr;
    char z = 90;
    
    for (int h = 0; h < t; h++) {
        string password;
        cin >> password;
        bool a = password[password.size() - 1] != z;
        bool b = false;
        // string p = insrt(password);
        cout << insrt(password) << endl;
        // cout << p << endl;
        // cout << time(password) << " " << time(p) << endl;
    }
}