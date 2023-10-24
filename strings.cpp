#include <iostream>
#include <string>
using namespace std;

int main() {
    string a;
    string b;
    
    cin >> a;
    cin >> b;
    
    cout << a.size() << " " << b.size() << "\n";
    cout << a + b << "\n";
    
    char a1 = a[0];
    char b1 = b[0];
    
    a[0] = b1;
    b[0] = a1;
    
    cout << a << " " << b;
    
    return 0;
}