#include <iostream>
#include <algorithm>
#include <string>

using namespace std;

// char 배열 대신 string


int main()
{
    string s ;
    cin >> s;
    cout << s << '\n';
    reverse(s.begin(), s.end()); // 뒤집기
    cout << s;


}