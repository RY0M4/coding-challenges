// Create a function taking a positive integer as its parameter and returning a string containing the Roman Numeral representation of that integer.

#include <iostream>
#include <string>

using namespace std;

#define M 1000
#define CM 900
#define D 500
#define CD 400
#define C 100
#define XC 90
#define L 50
#define XL 40
#define X 10
#define IX 9
#define V 5
#define IV 4
#define I 1

string int_to_roman_numeral(int n);

int main() {
    int n = 0;
    cout << "Insert an integer: ";
    cin >> n;
    cout << int_to_roman_numeral(n);
    return 0;
}

string int_to_roman_numeral(int n) {
    string s = "";
    while (n != 0) {
        if (n >= M) {
            n -= M;
            s += "M";
        } else if ( n >= CM) {
            n -= CM;
            s += "CM";
        } else if (n >= D) {
            n -= D;
            s += "D";
        } else if (n >= CD) {
            n -= CD;
            s += "CD";
        } else if (n >= C) {
            n -= C;
            s += "C";
        } else if (n >= XC) {
            n -= XC;
            s += "XC";
        } else if (n >= L) {
            n -= L;
            s += "L";
        } else if (n >= XL) {
            n -= XL;
            s += "XL";
        } else if (n >= X) {
            n -= X;
            s += "X";
        } else if (n >= IX) {
            n -= IX;
            s += "IX";
        } else if (n >= V) {
            n -= V;
            s += "V";
        } else if (n >= IV) {
            n -= IV;
            s += "IV";
        } else if (n >= I) {
            n -= I;
            s += "I";
        }
    }
    return s;
}
