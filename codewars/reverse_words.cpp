// Complete the function that accepts a string parameter, and reverses each word in the string. 

#include <iostream>
#include <string>
#include <vector>
#include <iterator>

using namespace std;

vector<string> tokenize_string(string s);
string reverse_string(string s);

int main() {
    string s = "";
    cout << "Insert a string: ";
    getline (cin, s);
    string new_s = "";
    for (const auto &str : tokenize_string(s)) {
        new_s += reverse_string(str);
    }
    cout << new_s;
    return 0;
}

vector<string> tokenize_string(string s) {
    vector<string> words{};
    string delim = " ";
    size_t pos = 0;
    while ((pos = s.find(delim)) != string::npos) {
        words.push_back(" " + s.substr(0, pos));
        s.erase(0, pos + delim.length());
    }
    if (!s.empty()) {
        words.push_back(s.substr(0, pos));
    }
    return words;
}

string reverse_string(string s) {
    string new_s = "";
    for (int i = s.length() - 1; i >= 0; i--) {
        new_s += s[i];
    }
    return new_s;
}
