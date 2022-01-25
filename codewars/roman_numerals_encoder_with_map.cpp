// Create a function taking a positive integer as its parameter and returning a string containing the Roman Numeral representation of that integer.

#include <iostream>
#include <map>

using namespace std;

int main() {
    map<int, string> bases = {{1000, "M"}, {900, "CM"}, {500, "D"}, {400, "CD"}, {100, "C"}, {90, "XC"}, {50, "L"}, {40, "XL"}, {10, "X"}, {9, "IX"}, {5, "V"}, {4, "IV"}, {1, "I"}};
    int n;
    cout << "Insert an integer: ";
    cin >> n;
    string s = "";
    auto map_iterator = bases.crbegin();
    while (map_iterator != bases.crend()) {
        if (n >= map_iterator->first) {
            n -= map_iterator->first;
            s += map_iterator->second;
        } else {
            map_iterator++;
        }
    }
    cout << s;
    return 0;
}
