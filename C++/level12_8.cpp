#include <iostream>

using namespace std;

int main(){

    int n,m;

    cin >> n >> m;

    string arr = "DATAPOWER";

    char s[9];

    int cnt = 0;
    for (int i = n; i < m+1; i++)
    {
        s[cnt] = arr[i];
        cnt++;
    }
    
    for (int i = 0; i < m+1; i++)
    {
        cout << s[i] ;
    }
    cout << "\n";

}