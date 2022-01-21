// Implement a function that adds two numbers together and returns their sum in binary. 

#include <iostream>
#include <string>

using namespace std;

unsigned long long sum(unsigned long long x, unsigned long long y);
string dec_to_bin(unsigned long long n);
string reverse_string(string s);

int main() {
    cout << dec_to_bin(sum(13819990972786524992, 3388125590936819485));
    return 0;
}

unsigned long long sum(unsigned long long x, unsigned long long y) {
    return x + y;
}

string dec_to_bin(unsigned long long n) {
    string bin = "";
    if (n == 0) {
        bin = "0";
    } else {
        while (n != 0) {
            if (n % 2 == 0) {
                bin += "0";
            } else {
                bin += "1";
            }
            n /= 2;
        }
    }
    return reverse_string(bin);
}

string reverse_string(string s) {
    string reverse_s = "";
    for (int i = s.length() - 1; i >= 0; i--) {
        reverse_s += s[i];
    }
    return reverse_s;
}
