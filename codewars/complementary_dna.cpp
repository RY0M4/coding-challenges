// In DNA strings, symbols "A" and "T" are complements of each other, as "C" and "G". 
// Your function receives one side of the DNA and you need to return the other complementary side.

#include <iostream>
#include <string>

using namespace std;

string process_string(string s);

int main() {
    string s;
    cout << "Insert a DNA strand: ";
    cin >> s;
    string processed_s = process_string(s);
    cout << processed_s;
    return 0;
}

string process_string(string s) {
    for (int i = 0; i < s.length(); i++) {
        if (s[i] == 'A') {
            s[i] = 'T';
        } else if (s[i] == 'T') {
            s[i] = 'A';            
        } else if (s[i] == 'G') {
            s[i] = 'C';
        } else if (s[i] == 'C') {
            s[i] = 'G';
        }
    }
    return s;
}
